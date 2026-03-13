from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app)

model = joblib.load("model/model2.pkl")

@app.route("/")
def home():
    return "House Price Prediction API is running!"

@app.route("/predict", methods = ["POST"])
def predict():
    try:
        data = request.json
        features = data["features"]
        prediction = model.predict([features])
        price = prediction[0]
        return jsonify({
            "Predicted_Price": float(price)
        })
    except Exception as e:
        return jsonify({
            "error":str(e)
        })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
