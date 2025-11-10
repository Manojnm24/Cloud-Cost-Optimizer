import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
import boto3

# 🔹 Step 1: Dummy training data
data = {
    "Date": pd.date_range(start="2024-05-01", periods=10, freq="MS"),
    "Cost": [10, 15, 20, 25, 22, 18, 30, 28, 35, 40]
}
df = pd.DataFrame(data)
df["Month"] = df["Date"].dt.month

X = df[["Month"]]
y = df["Cost"]

# 🔹 Step 2: Train simple regression model
model = LinearRegression()
model.fit(X, y)

# 🔹 Step 3: Save model as joblib file (cross-platform safe)
joblib.dump(model, "aws_cost_model.joblib")
print("✅ Model trained and saved locally as aws_cost_model.joblib")

# 🔹 Step 4: Upload to your S3 bucket
s3 = boto3.client('s3')
bucket_name = "cloud-cost-optimizer-manoj"
s3.upload_file("aws_cost_model.joblib", bucket_name, "models/aws_cost_model.joblib")

print(f"✅ Uploaded to s3://{bucket_name}/models/aws_cost_model.joblib")
