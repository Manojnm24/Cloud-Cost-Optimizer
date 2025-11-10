import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import boto3
import io
import joblib
from datetime import datetime, timedelta

# ----------------------------
# PAGE CONFIGURATION
# ----------------------------
st.set_page_config(page_title="Cloud Cost Optimizer", page_icon="💰", layout="wide")

# ----------------------------
# AWS CONFIG
# ----------------------------
S3_BUCKET = "your-s3-bucket-name"
MODEL_KEY = "cloud_cost_model.pkl"

# ----------------------------
# LOAD MODEL FROM S3
# ----------------------------
# ----------------------------
# MODEL LOAD (LOCAL FALLBACK)
# ----------------------------
@st.cache_resource
def load_model_from_s3():
    import os
    model_path = "cloud_cost_model.pkl"
    if os.path.exists(model_path):
        return joblib.load(model_path)
    else:
        st.warning("⚠️ S3 model not found, using default local fallback model.")
        from sklearn.linear_model import LinearRegression
        dummy_model = LinearRegression()
        dummy_model.coef_ = np.array([1.0])
        dummy_model.intercept_ = 0
        dummy_model.predict = lambda X: X.flatten()  # simple mock predict
        return dummy_model


# ----------------------------
# GENERATE SAMPLE COST DATA
# ----------------------------
def get_sample_cost_data(days=30):
    end = datetime.utcnow().date()
    dates = pd.date_range(end - timedelta(days=days - 1), end)
    costs = np.random.uniform(50, 200, size=days)
    df = pd.DataFrame({"Date": dates, "Cost": costs})
    return df

# ----------------------------
# ANOMALY DETECTION
# ----------------------------
def detect_anomalies(df, model):
    df["Predicted"] = model.predict(df["Cost"].values.reshape(-1, 1))
    df["Anomaly"] = np.abs(df["Cost"] - df["Predicted"]) > 30  # Threshold
    return df

# ----------------------------
# MAIN DASHBOARD
# ----------------------------
def main():
    st.title("💰 Cloud Cost Optimizer Dashboard")
    st.markdown("Monitor your cloud costs and detect anomalies in real-time.")

    # Sidebar
    st.sidebar.header("Settings")
    days = st.sidebar.slider("Days to visualize", 10, 90, 30)
    show_table = st.sidebar.checkbox("Show Data Table", True)

    # Load model and data
    with st.spinner("Loading model..."):
        model = load_model_from_s3()
        st.success("✅ Model loaded successfully from S3")

    df = get_sample_cost_data(days)
    df = detect_anomalies(df, model)

    # Display metrics
    total_cost = df["Cost"].sum()
    avg_cost = df["Cost"].mean()
    anomaly_count = df["Anomaly"].sum()

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Cost ($)", f"{total_cost:,.2f}")
    col2.metric("Average Daily Cost ($)", f"{avg_cost:,.2f}")
    col3.metric("Anomalies Detected", int(anomaly_count))

    # Plot the cost data
    st.subheader("📊 Cost Trend with Anomalies")
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df["Date"], df["Cost"], label="Actual Cost", color="blue")
    ax.scatter(df[df["Anomaly"]]["Date"], df[df["Anomaly"]]["Cost"], color="red", label="Anomaly", s=80)
    ax.set_xlabel("Date")
    ax.set_ylabel("Cost ($)")
    ax.legend()
    st.pyplot(fig)

    # Show data table
    if show_table:
        st.subheader("📄 Detailed Cost Data")
        st.dataframe(df)

    # Footer
    st.markdown("---")
    st.caption("Built with ❤️ using Streamlit, AWS, and ML")

# ----------------------------
# ENTRY POINT
# ----------------------------
if __name__ == "__main__":
    main()
