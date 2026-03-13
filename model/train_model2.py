import pandas as pd
import joblib
from sklearn.linear_model import LinearRegression

data = pd.read_csv("model/AmesHousing.csv")
# print(data.head())
print(data.columns)

data["Lot Shape"] = data["Lot Shape"].map({
    "Reg": 0,
    "IR1": 1,
    "IR2": 2,
    "IR3": 3
})

features = [
    "Overall Qual",   # overall house quality
    "Gr Liv Area",    # living area size
    "Garage Cars",    # garage capacity
    "Garage Area",    # garage area
    "Total Bsmt SF",  # basement area
    "1st Flr SF",     # first floor area
    "Full Bath",      # number of bathrooms
    "TotRms AbvGrd",  # total rooms above ground
    "Year Built",      # construction year
    "Lot Shape"         #IR1 or Reg
]

x = data[features]
x = x.fillna(0)
y = data["SalePrice"]

model = LinearRegression()
model.fit(x,y)
print("Model trained successfully")
joblib.dump(model,"model/model2.pkl")
print("Model saved successfully")

prediction = model.predict(x.head())
print("Sale price : ", prediction)

