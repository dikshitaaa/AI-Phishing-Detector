from flask import Flask, render_template, request
import pickle
import re
import requests

app = Flask(__name__)

with open('ai_model.pkl', 'rb') as file:
    model = pickle.load(file)

def extract_features(url):
    features = []
    features.append(len(url)) 
    features.append(1 if re.match(r'^https?://', url) else 0) 
    features.append(url.count('@')) 
    features.append(len(re.findall(r'login|secure|update|bank|confirm|account|verify', url.lower()))) 
    features.append(url.count('/')) 
    features.append(1 if 'https' in url else 0) 
    features.append(url.count('.')) 
    features.append(url.count('-')) 
    features.append(url.count('and')) 
    features.append(url.count('or')) 
    features.append(url.count('www')) 
    features.append(url.count('.com')) 
    features.append(url.count('_')) 
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

    if not url_input.startswith('http'):
        url_input = 'http://' + url_input

    try:
        input_data = extract_features(url_input)
        prediction = model.predict([input_data])[0]
        
        # Calculate Risk Score (0 to 100)
        risk_score = 10
        reasons = []
        if input_data[0] > 75: risk_score += 20; reasons.append("URL is unusually long")
        if input_data[2] > 0: risk_score += 30; reasons.append("Contains '@' symbol (Red Flag)")
        if input_data[3] > 0: risk_score += 25; reasons.append("Contains sensitive keywords")
        if input_data[5] == 0: risk_score += 15; reasons.append("No HTTPS encryption")
        if input_data[6] > 4: risk_score += 10; reasons.append("Excessive dots in domain")
        
        if risk_score > 100: risk_score = 100
        if prediction == 0 and risk_score > 60: risk_score = 40 # Safe override
        
        # Live Ping check
        live_status = "Inactive"
        try:
            res = requests.get(url_input, timeout=2)
            live_status = f"Active (HTTP {res.status_code})"
        except:
            live_status = "Unreachable / Dead"

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