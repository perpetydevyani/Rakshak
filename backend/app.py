from flask import Flask, request, jsonify
from flask_cors import CORS
from risk_model import predict_risk
from fraud_detection import detect_fraud
from pricing import calculate_premium

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return {"message": "Rakshak API Running"}

@app.route("/predict-risk", methods=["POST"])
def risk():
    data = request.json
    weather = data["weather"]
    pollution = data["pollution"]

    risk_score = predict_risk(weather, pollution)
    premium = calculate_premium(risk_score)

    return jsonify({
        "risk_score": risk_score,
        "weekly_premium": premium
    })

@app.route("/check-fraud", methods=["POST"])
def fraud():
    data = request.json
    speed = data["speed"]
    movement_pattern = data["pattern"]

    fraud_score = detect_fraud(speed, movement_pattern)

    return jsonify({
        "fraud_score": fraud_score
    })

if __name__ == "__main__":
    app.run(debug=True)
