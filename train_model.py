import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
import joblib

# Load dataset
data = pd.read_csv("commute_data.csv")

# Encode text columns
le_time = LabelEncoder()
le_transport = LabelEncoder()
le_day = LabelEncoder()
le_risk = LabelEncoder()

data["time_of_day"] = le_time.fit_transform(data["time_of_day"])
data["transport"] = le_transport.fit_transform(data["transport"])
data["day_type"] = le_day.fit_transform(data["day_type"])
data["risk"] = le_risk.fit_transform(data["risk"])

X = data[["time_of_day", "transport", "day_type", "delay_minutes"]]
y = data["risk"]

# Train model
model = DecisionTreeClassifier()
model.fit(X, y)

# Save model and encoders
joblib.dump(model, "model.pkl")
joblib.dump((le_time, le_transport, le_day, le_risk), "encoders.pkl")

print("✅ Model trained and saved successfully!")
