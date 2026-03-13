
## Input Features

| Feature | Description | Range |
|------|------|------|
MedInc | Median income | 0.5 – 15 |
HouseAge | House age | 1 – 52 |
AveRooms | Average rooms | 1 – 15 |
AveBedrms | Average bedrooms | 0.5 – 5 |
Population | Population | 3 – 35682 |
AveOccup | Average occupancy | 1 – 10 |
Latitude | Latitude | 32 – 42 |
Longitude | Longitude | -124 – -114 |

Values outside these ranges may produce unrealistic predictions.

---

# House Price Prediction using Machine Learning

A full-stack Machine Learning web application that predicts house prices using the California Housing dataset.

The project includes:

• A trained Machine Learning model  
• A Flask backend API  
• A frontend interface built with HTML, CSS, and JavaScript  

Users can input housing features and receive a predicted house price.

---

## Application Preview

![House Price Predictor](assets/UI.png)

## Project Architecture

Frontend (HTML, CSS, JavaScript)
        ↓
Flask API (Python)
        ↓
Machine Learning Model (Scikit-Learn)
        ↓
Prediction Output

---

## Dataset

This project uses the **California Housing dataset** from Scikit-Learn.

The dataset contains information about housing blocks in California including income, location, population, and housing characteristics.

Target variable:

MedHouseVal → Median house value (in units of $100,000)

Example:

Prediction = 4.11  
Actual price = $411,000

---

## Example Input

MedInc: 8.3  
HouseAge: 41  
AveRooms: 6.9  
AveBedrms: 1  
Population: 322  
AveOccup: 2.5  
Latitude: 37.88  
Longitude: -122.23  

Predicted Price ≈ $411,000

---

## Technologies Used

Python  
Flask  
Scikit-Learn  
HTML  
CSS  
JavaScript

---

## Installation

Clone the repository:
