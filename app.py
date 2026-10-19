from flask import Flask, render_template, request
import pickle
import re
import requests

app = Flask(__name__)

# Load AI Model
with open('ai_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Trusted domains ki list (Whitelist)
trusted_domains = ['google.com', 'youtube.com', 'facebook.com', 'amazon.com', 'wikipedia.org', 'github.com', 'microsoft.com', 'linkedin.com']

def extract_features(url):
    features = []
    features.append(len(url)) # url_length
    features.append(1 if re.match(r'^https?://', url) else 0) # valid_url
    features.append(url.count('@')) # at_symbol
    features.append(len(re.findall(r'login|secure|update|bank|confirm|account|verify', url.lower()))) # sensitive_words
    features.append(url.count('/')) # path_length
    features.append(1 if 'https' in url else 0) # isHttps
    features.append(url.count('.')) # nb_dots
    features.append(url.count('-')) # nb_hyphens
    features.append(url.count('and')) # nb_and
    features.append(url.count('or')) # nb_or
    features.append(url.count('www')) # nb_www
    features.append(url.count('.com')) # nb_com
    features.append(url.count('_')) # nb_underscore
    return features

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    data = request.get_json()
    url_input = data.get('url', '').strip()
    
    if not url_input:
        return {"error": "Please provide a URL"}

    # Ensure URL has scheme
    if not url_input.startswith('http'):
        url_input = 'https://' + url_input

    try:
        input_data = extract_features(url_input)
        prediction = model.predict([input_data])[0]
        
        # Calculate Risk Score & Reasons
        risk_score = 10
        reasons = []
        
        if input_data[0] > 75: risk_score += 20; reasons.append("URL is unusually long")
        if input_data[2] > 0: risk_score += 30; reasons.append("Contains '@' symbol (Red Flag)")
        if input_data[3] > 0: risk_score += 25; reasons.append("Contains sensitive keywords")
        if input_data[5] == 0: risk_score += 15; reasons.append("No HTTPS encryption")
        if input_data[6] > 4: risk_score += 10; reasons.append("Excessive dots in domain")
        
        if risk_score > 100: risk_score = 100
        
        # Live Ping check
        live_status = "Inactive"
        is_live = False
        try:
            res = requests.get(url_input, timeout=3)
            live_status = f"Active (HTTP {res.status_code})"
            is_live = True
        except:
            live_status = "Unreachable / Dead"

        # --- SMART FIX LOGIC ---
        # 1. Agar trusted domain hai, toh pakka Safe hai
        is_trusted = any(domain in url_input.lower() for domain in trusted_domains)
        
        if is_trusted:
            prediction = 0
            risk_score = 5
        # 2. Agar AI ne Phishing bola, par humare rules ko koi khatra nahi mila, aur site live hai
        elif prediction == 1 and len(reasons) == 0 and is_live:
            prediction = 0
            risk_score = 15
        # 3. Agar rules ne koi khatra bataya hai, toh force Phishing
        elif len(reasons) > 0:
            prediction = 1
            if risk_score < 50: risk_score = 50

        return {
            "status": "Safe" if prediction == 0 else "Phishing",
            "score": risk_score,
            "reasons": reasons if reasons else ["No suspicious patterns found"],
            "live_status": live_status
        }
    except Exception as e:
        return {"error": str(e)}

if __name__ == '__main__':
    app.run(debug=True)