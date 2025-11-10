# Cloud-Cost-Optimizer
Cloud Cost Optimizer is an AI-powered tool that analyzes and visualizes your AWS cloud spending to detect anomalies and optimize costs. It provides an interactive Streamlit dashboard and a trained ML model for intelligent cost monitoring and prediction.

### 🔍 Overview
The **Cloud Cost Optimizer** is a machine learning–powered dashboard that analyzes your cloud spending patterns, detects anomalies, and visualizes daily cost trends.  
It helps AWS users proactively identify unusual cost spikes and optimize their cloud resource usage.

---

### 🚀 Features
- ✅ Fetches AWS cloud cost history automatically  
- 📊 Detects daily anomalies using trained ML models  
- 📈 Interactive Streamlit dashboard for visualization  
- ☁️ Model stored and loaded from S3  
- 🧠 Easily retrain model using `train_model.py`

---

### 🧩 Project Structure

CloudCostOptimizer/
│
├── app.py # Backend logic – loads model, fetches data, detects anomalies
├── dashboard_app.py # Streamlit dashboard
├── train_model.py # Model training script
├── aws_cost_model.pkl # Pre-trained ML model
├── aws_cost_history.csv # Example dataset
├── requirements.txt # Python dependencies
└── model/ # Optional model backups
