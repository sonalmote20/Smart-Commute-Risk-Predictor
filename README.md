# 🚦 Smart Commute Risk Predictor

### AI/ML-Powered Urban Commute Risk Prediction System

An AI/ML-based web application that predicts the **risk level of an urban commute before the journey starts**, helping commuters make smarter travel decisions and reduce uncertainty.

---

## 🌐 Live Demo

🚀 **Try the application:**  
https://smart-commute-risk-predictor.onrender.com

💻 **Source Code:**  
https://github.com/sonalmote20/Smart-Commute-Risk-Predictor

---

## 📌 Problem Statement

Urban commuting can be unpredictable due to peak-hour congestion, transport delays, overcrowding, and unexpected disruptions.

Commuters often discover these problems **only after starting their journey**, which can lead to:

- Missed connections
- Increased travel time
- Stress and inconvenience
- Difficulty choosing the best transport option

The goal of this project is to provide a simple predictive system that helps commuters **anticipate commute risk before travelling**.

---

## 💡 Solution

**Smart Commute Risk Predictor** uses Machine Learning to analyze commute-related inputs and classify the journey into a risk category.

The current model considers:

- 🕐 Time of day
- 🚆 Transport mode
- 📅 Day type
- ⏱️ Expected delay

The system provides a simple risk prediction:

| Risk Level | Meaning |
|---|---|
| 🟢 Low | Relatively safe and predictable commute |
| 🟡 Medium | Some possibility of delay or disruption |
| 🔴 High | Higher likelihood of commute problems |

This prediction can help users make better travel decisions and consider alternative options.

---

## 🧠 AI/ML Implementation

The project uses a **Decision Tree Classifier** for supervised machine learning.

### ML Pipeline

```text
User Input
    ↓
Data Preprocessing
    ↓
Label Encoding
    ↓
Trained Decision Tree Model
    ↓
Risk Prediction
    ↓
Low / Medium / High