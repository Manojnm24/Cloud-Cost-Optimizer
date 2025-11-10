import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import boto3
import joblib
import io
from datetime import datetime, timedelta

# -----------------------
# Load model from S3
# -----------------------
def load_model_from_s3():
    s3 = boto3.client('s3')
    bucket_name = 'cloud-cost-optimizer-manoj'
    model_key = 'models/aws_cost_model.joblib'

    response = s3.get_object(Bucket=bucket_name, Key=model_key)
    model_data = response['Body'].read()
    model = joblib.load(io.BytesIO(model_data))
    return model

# -----------------------
# Simulated AWS cost data
# -----------------------
def fetch_cost_data():
    end = datetime.utcnow().date()
    start = end - timedelta(days=29)
    dates = pd.date_range(start=start, end=end, freq='D')
    costs = [round(5 + (i % 7) * 0.2, 2) for i in range(len(dates))]
    df = pd.DataFrame({'Date': dates, 'Cost': costs})
    return df

# -----------------------
# Detect anomalies
# -----------------------
def detect_anomalies(df, model):
    df['Prediction'] = model.predict(df[['Cost']])
    df['Anomaly'] = abs(df['Cost'] - df['Prediction']) > 0.5
    return df

# -----------------------
# Streamlit UI
# -----------------------
def main():
    st.set_page_config(page_title="☁️ Cloud Cost Optimizer Dashboard", layout="wide")

    st.title("☁️ Cloud Cost Optimizer Dashboard")
    st.markdown("Monitor AWS spending trends, detect anomalies, and visualize predictions.")

    with st.spinner("Loading model from S3..."):
        model = load_model_from_s3()
    st.success("✅ Model loaded successfully from S3")

    df = fetch_cost_data()
    st.write(f"📅 Showing last {len(df)} days of AWS cost data")

    df = detect_anomalies(df, model)

    # Plotting
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df['Date'], df['Cost'], label='Actual Cost', color='blue')
    ax.plot(df['Date'], df['Prediction'], label='Predicted Cost', color='orange')
    ax.scatter(df.loc[df['Anomaly'], 'Date'], df.loc[df['Anomaly'], 'Cost'], color='red', label='Anomaly')
    ax.set_title("AWS Cost Trend with Anomalies")
    ax.set_xlabel("Date")
    ax.set_ylabel("Cost (USD)")
    ax.legend()

    st.pyplot(fig)

    # Show anomaly table
    st.subheader("🚨 Anomaly Details")
    st.dataframe(df[df['Anomaly']])

    st.success("Dashboard loaded successfully ✅")

if __name__ == "__main__":
    main()
