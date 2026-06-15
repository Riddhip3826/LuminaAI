import argparse
import pandas as pd
import joblib

parser = argparse.ArgumentParser()
parser.add_argument("--features", required=True)
parser.add_argument("--model", required=True)
parser.add_argument("--output", required=True)
args = parser.parse_args()

model = joblib.load(args.model)

X = pd.read_csv(args.features)

predictions = model.predict(X)

out = pd.DataFrame({
    "Predicted_Revenue": predictions
})

out.to_csv(args.output, index=False)

print("Predictions created successfully.")
