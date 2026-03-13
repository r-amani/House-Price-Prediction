# 🏠 House Price Prediction Web App

A full-stack Machine Learning web application that predicts house prices based on housing features.
The project uses a trained Linear Regression model and provides predictions through a Flask API with a responsive frontend.

---
## Application Preview 

![House Price Predictor](assets/UI(2).png)

---

# 🚀 Live Backend API

Deployed using Render:

https://house-price-prediction-8hdv.onrender.com

---

# 📌 Project Overview

This project demonstrates an **end-to-end Machine Learning pipeline**, including:

* Data preprocessing
* Feature selection
* Model training
* Backend API creation
* Frontend interface
* Deployment

Users can enter housing features such as living area, garage size, number of rooms, etc., and the model predicts the estimated house price.

---

# 🧠 Machine Learning Model

Model Used:

Linear Regression

Dataset:

Ames Housing Dataset

Selected Features:

* Overall Qual
* Gr Liv Area
* Garage Cars
* Garage Area
* Total Bsmt SF
* 1st Flr SF
* Full Bath
* TotRms AbvGrd
* Year Built
* Lot Shape

Target Variable:

SalePrice

---

# 🏗️ Tech Stack

Frontend

* HTML
* CSS
* JavaScript

Backend

* Python
* Flask
* Flask-CORS

Machine Learning

* scikit-learn
* pandas
* joblib

Deployment

* Render

Version Control

* Git
* GitHub

---

# 📂 Project Structure

```
House-Price-Prediction
│
├── backend
│   └── app.py
│
├── model
│   └── model2.pkl
│
├── index.html
├── style.css
├── script.js
│
├── train_model.py
├── AmesHousing.csv
│
└── README.md
```

---

# ⚙️ How It Works

1. The user enters house features in the frontend form.

2. The frontend sends a POST request to the Flask API.

3. The backend loads the trained model and predicts the price.

4. The predicted price is returned as JSON.

5. The frontend displays the estimated price.

---

# 📊 Example Input

```
Overall Quality: 7
Living Area: 1800
Garage Cars: 2
Garage Area: 500
Basement Area: 900
1st Floor Area: 1200
Bathrooms: 2
Rooms: 7
Year Built: 2005
Lot Shape: Regular
```

Example Output:

```
Estimated Price: $215,000
```

---

# 🖥️ Running the Project Locally

### 1️⃣ Clone the repository

```
git clone https://github.com/r-amani/House-Price-Prediction.git
```

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Run the backend server

```
python backend/app.py
```

### 4️⃣ Open the frontend

Open:

```
index.html
```

in your browser.

---

# ✨ Features

* Machine Learning prediction model
* Flask REST API
* Responsive frontend interface
* Real-time price prediction
* Deployment-ready project structure

---

# 📈 Future Improvements

* Add more housing features
* Improve model accuracy using Random Forest or XGBoost
* Deploy frontend with GitHub Pages
* Add interactive data visualizations

---

# 👨‍💻 Author

Sujan Ramani

Computer Science Student

---

# 📜 License

This project is for educational and portfolio purposes.
