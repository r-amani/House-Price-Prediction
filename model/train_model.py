import joblib
from sklearn.datasets import fetch_california_housing  
from sklearn.linear_model import LinearRegression

data = fetch_california_housing(as_frame=True)
# print(data.frame.head())
# print(data.frame.columns)
df = data.frame

x = df.drop("MedHouseVal", axis = 1)
y = df["MedHouseVal"]

# print(x.head())
# print(y.head())


model = LinearRegression()
model.fit(x,y)
print("Model trained successfully")
joblib.dump(model, "model/model.pkl")
print("Model saved successfully")



prediction = model.predict(x.head())
print("Predictions prices ($) : ", prediction*100000)

