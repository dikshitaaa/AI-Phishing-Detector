# 🛡️ PhishGuard Pro: AI-Powered Phishing URL Detector

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Framework-Flask-green.svg)
![Scikit-Learn](https://img.shields.io/badge/ML-Scikit--Learn-orange.svg)
![License](https://img.shields.io/badge/License-MIT-brightgreen.svg)

**PhishGuard Pro** is an advanced AI-driven web application designed to detect malicious and phishing URLs in real-time. It uses a Machine Learning model (Random Forest) combined with dynamic feature extraction (Regex) to analyze the structure of a URL and predict whether it is safe or a threat.

## ✨ Key Features

*   **Real-time Analysis:** Instantly scans any URL pasted by the user without reloading the page (AJAX integration).
*   **Dynamic Feature Extraction:** Automatically parses the URL to extract 13+ security parameters (length, special characters, sensitive keywords, HTTPS status) using Regex.
*   **Explainable AI (XAI):** If a URL is flagged as malicious, the system provides specific reasons (e.g., "Contains @ symbol", "No HTTPS encryption") to help users understand the threat.
*   **Risk Scoring Dashboard:** Calculates a risk score from 0 to 100 and displays a modern, cyber-security-themed dashboard.
*   **Live HTTP Check:** Uses Python's `requests` library to ping the URL and check if the website is actually live.

## 📸 Screenshots

Here is a preview of the PhishGuard Pro Dashboard:

![PhishGuard Dashboard](screenshots/demo.png)

## 🛠️ Tech Stack

*   **Frontend:** HTML5, CSS3, Vanilla JavaScript (Dark Theme UI)
*   **Backend:** Python (Flask)
*   **Machine Learning:** Scikit-learn (Random Forest Classifier), Pandas, NumPy
*   **Libraries:** Requests, Pickle, Re (Regex)

## 📂 Project Structure

```text
AI-URL-detector/
│
├── templates/
│   └── index.html           # Frontend UI
├── screenshots/
│   └── demo.png             # Project UI Screenshot
├── AI_Model_Training.ipynb  # Jupyter Notebook (Model Training)
├── app.py                   # Flask Backend Server
├── ai_model.pkl             # Trained ML Model
├── phishing_url_dataset.csv # Dataset used for training
└── README.md                # Project Documentation

🚀 How to Run Locally
Clone the repository:

bash
git clone https://github.com/dikshitaaa/AI-URL-detector.git
cd AI-URL-detector
Install dependencies:

bash
pip install flask pandas scikit-learn requests
Run the application:

bash
python app.py
Open in Browser:
Go to http://127.0.0.1:5000
