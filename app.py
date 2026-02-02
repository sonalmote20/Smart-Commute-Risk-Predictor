from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load model & encoders
model = joblib.load("model.pkl")
le_time, le_transport, le_day, le_risk = joblib.load("encoders.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    time = le_time.transform([data["time_of_day"]])[0]
    transport = le_transport.transform([data["transport"]])[0]
    day = le_day.transform([data["day_type"]])[0]
    delay = data["delay_minutes"]

    prediction = model.predict([[time, transport, day, delay]])
    risk_level = le_risk.inverse_transform(prediction)[0]

    return jsonify({
        "Predicted Risk Level": risk_level
    })

if __name__ == "__main__":
    app.run(debug=True)
