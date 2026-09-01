# 🚦 Smart Commute Risk Predictor

### AI/ML-Powered Urban Commute Risk Prediction System

An AI/ML-based web application that predicts the **risk level of an urban commute** before the journey starts using time of day, transport mode, day type, and expected delay.

## 🌐 Live Demo

🚀 **Live Website:**  
https://smart-commute-risk-predictor.onrender.com

💻 **GitHub Repository:**  
https://github.com/sonalmote20/Smart-Commute-Risk-Predictor

---

## 📌 Problem

Urban commuting can be unpredictable due to traffic, delays, overcrowding, and unexpected disruptions. Commuters need a simple way to understand potential travel risk before starting their journey.

## 💡 Solution

Smart Commute Risk Predictor uses Machine Learning to classify a journey as:

🟢 **Low Risk**  
🟡 **Medium Risk**  
🔴 **High Risk**

### Input Features

- 🕐 Time of Day
- 🚆 Transport Mode
- 📅 Day Type
- ⏱️ Expected Delay

---

## 🧠 AI/ML

The system uses a **Decision Tree Classifier** with Label Encoding.

```text
User Input
    ↓
Preprocessing
    ↓
Label Encoding
    ↓
Decision Tree Model
    ↓
Risk Prediction
    ↓
Low / Medium / High

📂 Project Structure
Smart-Commute-Risk-Predictor/
│
├── app.py
├── train_model.py
├── commute_data.csv
├── model.pkl
├── encoders.pkl
├── requirements.txt
├── README.md
│
└── templates/
    └── index.html

⚙️ Run Locally
git clone https://github.com/sonalmote20/Smart-Commute-Risk-Predictor.git
cd Smart-Commute-Risk-Predictor
pip install -r requirements.txt
python app.py

Open:

http://127.0.0.1:10000

👩‍💻 Author

Sonal Mote
B.Tech Information Technology Student
