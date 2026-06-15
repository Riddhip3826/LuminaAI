import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

df = pd.read_csv("data/sample_data.csv")

df["Channel_Code"] = df["Channel"].astype("category").cat.codes

X = df[["Spend", "ROAS", "Channel_Code"]]
y = df["Revenue"]

model = RandomForestRegressor(random_state=42)
model.fit(X, y)

joblib.dump(model, "pickle/model.pkl")

print("Model trained and saved.")
