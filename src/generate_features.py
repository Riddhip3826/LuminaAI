import argparse
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument("--data-dir", required=True)
parser.add_argument("--out", required=True)
args = parser.parse_args()

df = pd.read_csv(f"{args.data_dir}/sample_data.csv")

df["Channel_Code"] = df["Channel"].astype("category").cat.codes

features = df[["Spend", "ROAS", "Channel_Code"]]

features.to_csv(args.out, index=False)

print("Features generated successfully.")
