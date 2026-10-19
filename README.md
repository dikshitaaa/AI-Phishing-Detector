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
*   **Smart Override Logic:** Includes a whitelist for trusted domains (like Google, GitHub) and a smart verification system to prevent false positives on legitimate live websites.
*   **Live HTTP Check:** Uses Python's `requests` library to ping the URL and check if the website is actually live.

## 📸 Screenshots

**1. Legitimate URL Analysis (Safe)**
![Safe URL Analysis](screenshots/legitimate.png)

**2. Phishing URL Analysis (Threat Detected)**
![Phishing URL Analysis](screenshots/fake.png)

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
│   ├── legitimate.png       # Safe URL result screenshot
│   └── fake.png             # Phishing URL result screenshot
├── AI_Model_Training.ipynb  # Jupyter Notebook (Model Training)
├── app.py                   # Flask Backend Server
├── ai_model.pkl             # Trained ML Model
├── phishing_url_dataset.csv # Dataset used for training
└── README.md                # Project Documentation
