🚦 Smart Commute Risk Predictor (AI/ML)

An AI/ML-based system that predicts the risk level of an urban commute before the journey starts, helping commuters make smarter decisions and reduce uncertainty in daily travel.

📌 Problem Statement

Urban commuting in Indian cities is highly unpredictable due to fragmented transport systems, peak-hour congestion, and lack of end-to-end visibility.
Commuters often discover delays, overcrowding, or disruptions only after starting their journey, leading to stress, missed connections, and loss of productivity.

The core problem is not the lack of transport options, but the absence of a unified, predictive system that helps commuters anticipate issues before travel.

💡 Solution Overview

Smart Commute Risk Predictor uses Machine Learning to analyze historical commute patterns and predict the risk level of a journey based on:

Time of day

Transport mode

Day type (weekday/weekend)

Expected delay

The system outputs a clear and simple risk classification:

🟢 Low Risk

🟡 Medium Risk

🔴 High Risk

This allows users to adjust departure time, change transport modes, or plan alternatives in advance.

🧠 How AI/ML Is Used

A supervised Machine Learning model (Decision Tree Classifier) is trained on historical/synthetic commute data.

Categorical inputs are encoded using Label Encoding.

The trained model predicts the commute risk level for new journey inputs.

The model is exposed via a Flask API for real-time predictions.

🛠️ Tech Stack

Programming Language: Python

Machine Learning: Scikit-learn

Data Handling: Pandas

Backend/API: Flask

Model Storage: Joblib

Testing Tool: Thunder Client / Postman

📂 Project Structure
SmartCommuteAI/
│── app.py              # Flask API for predictions
│── train_model.py      # ML model training script
│── commute_data.csv    # Dataset (synthetic)
│── model.pkl           # Trained ML model
│── encoders.pkl        # Label encoders
│── README.md           # Project documentation

⚙️ How to Run the Project Locally
1️⃣ Install Dependencies
pip install pandas scikit-learn flask joblib

2️⃣ Train the Model
python train_model.py


This will generate:

model.pkl

encoders.pkl

3️⃣ Start the Flask Server
python app.py


Server will run at:

http://127.0.0.1:5000

4️⃣ Test the API (Using Thunder Client / Postman)

Endpoint

POST /predict


Request Body (JSON)

{
  "time_of_day": "morning",
  "transport": "train",
  "day_type": "weekday",
  "delay_minutes": 20
}


Response

{
  "Predicted Risk Level": "high"
}

🎯 Use Cases

Daily office or college commuters

Smart city mobility platforms

Transport authorities for demand analysis

Decision-support systems for urban travel planning

🚀 Future Enhancements

Real-time data integration (GPS, traffic, weather)

Delay prediction in minutes using regression models

Crowd density prediction

Web/mobile user interface

Integration with public transport apps

City-level analytics dashboard for authorities

🏆 Hackathon Value

Solves a real-world urban mobility problem

Uses AI/ML meaningfully (prediction, not just UI)

Easy to demo and explain

Scalable and extensible

Strong alignment with smart city initiatives

👩‍💻 Author

Sonal Mote
B.Tech IT Student

