# ☁️ Cloud Cost Optimizer
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

```
CloudCostOptimizer/
├── app.py # Backend logic – loads model, fetches data, detects anomalies
├── dashboard_app.py # Streamlit dashboard
├── train_model.py # Model training script
├── aws_cost_model.pkl # Pre-trained ML model
├── aws_cost_history.csv # Example dataset
├── requirements.txt # Python dependencies
└── model/ # Optional model backups
```

---

### ⚙️ Installation & Setup

- 1️⃣ Clone the Repository
```
git clone https://github.com/<your-username>/CloudCostOptimizer.git
cd CloudCostOptimizer
```

- 2️⃣ Create and Activate Virtual Environment
Windows (PowerShell)
```
python -m venv venv
venv\Scripts\activate
```
for Ubuntu / macOS
```
python3 -m venv venv
source venv/bin/activate
```
- 3️⃣ Install Dependencies
```
pip install -r requirements.txt
```
- ▶️ Running the Application
Run Backend Analyzer
```
python app.py
```
- Launch Streamlit Dashboard
```
streamlit run dashboard_app.py
```

- Then open your browser at 👉 http://localhost:8501

🧠 Training a New Model

- If you want to retrain the model with new AWS cost data:
```
python train_model.py
```

- This will generate a new aws_cost_model.pkl and automatically upload it to S3.

---

### 🛠️ Tech Stack

- Python 3.10+

- Streamlit – Interactive dashboard

- Scikit-learn – ML model

- Pandas – Data processing

- Matplotlib – Visualization

- Boto3 – AWS S3 integration

- Joblib – Model serialization

---

### 📦 Requirements
```
streamlit
pandas
scikit-learn
matplotlib
boto3
joblib
```
---

### 🏗️ Future Enhancements

- 🔄 Multi-cloud support (Azure, GCP)
- 📬 Email alerts for anomaly detection
- 📉 Predictive forecasting for upcoming costs

---

#### ✅ Example Command Summary
- Action	Command
- Clone repo	git clone <repo-url>
- Create venv	python -m venv venv
- Activate venv	venv\Scripts\activate (Win) / source venv/bin/activate (Linux)
- Install reqs	pip install -r requirements.txt
- Run backend	python app.py
- Run dashboard	streamlit run dashboard_app.py
- Retrain model	python train_model.py

