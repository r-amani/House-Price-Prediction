from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app)

model = joblib.load("model/model.pkl")

@app.route("/predict", methods = ["POST"])
def predict():
    data = request.json
    features = data["features"]
    prediction = model.predict([features])
    price = prediction[0]*100000
    return jsonify({
        "Predicted_Price": float(price)
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
