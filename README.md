# 📱 AI-Powered Mobile Addiction Risk Prediction System

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green?logo=fastapi)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange?logo=scikitlearn)
![MLflow](https://img.shields.io/badge/MLflow-Experiment%20Tracking-blue)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker)
![CI/CD](https://img.shields.io/badge/GitHub-Actions-black?logo=githubactions)
![License](https://img.shields.io/badge/License-MIT-success)

</p>

---

## 📌 Project Overview

The **AI-Powered Mobile Addiction Risk Prediction System** is an end-to-end Machine Learning solution designed to estimate a user's daily screen time and evaluate their mobile addiction risk using behavioral and device usage patterns.

The project combines **data preprocessing, feature engineering, machine learning, experiment tracking, API deployment, and containerization** to deliver a production-ready prediction service.

Instead of simply predicting screen time, the system categorizes users into **Low**, **Medium**, or **High Addiction Risk** and provides personalized digital wellness recommendations.

---

# 🎯 Problem Statement

Excessive smartphone usage has become one of the biggest digital wellness challenges worldwide.

Organizations, researchers, healthcare providers, and educational institutions need intelligent systems capable of identifying high-risk users before excessive usage negatively impacts productivity, mental health, and lifestyle.

Traditional monitoring methods are often manual and reactive.

This project provides an AI-driven predictive solution that automatically estimates addiction risk using mobile usage behavior.

---

# 💡 Solution

This system leverages Machine Learning to learn behavioral patterns from smartphone usage data.

After preprocessing the data and engineering meaningful features, the trained model predicts expected screen time and classifies users into different addiction risk categories.

The prediction service is exposed through a FastAPI REST API, making it easy to integrate with web, mobile, or enterprise applications.

---

# ✨ Key Features

- Predicts daily mobile screen time
- Mobile addiction risk classification
- Personalized wellness recommendations
- Feature engineering pipeline
- REST API using FastAPI
- MLflow experiment tracking
- Docker containerization
- CI/CD with GitHub Actions
- Production-ready deployment structure
- Scalable API architecture

---

# 🛠️ Tech Stack

| Category | Technologies |
|-----------|-------------|
| Programming Language | Python |
| Machine Learning | Scikit-Learn, XGBoost, LightGBM, CatBoost |
| Data Analysis | Pandas, NumPy |
| API | FastAPI |
| Model Serialization | Joblib |
| Experiment Tracking | MLflow |
| Containerization | Docker |
| CI/CD | GitHub Actions |
| Deployment | Uvicorn |
| Notebook | Jupyter |

---

# 📂 Project Structure

```text
AI-Powered-Mobile-Addiction-Risk-Prediction-System
│
├── app.py
├── preprocessing.py
├── model_training.py
├── model_testing.py
├── feature_importance.py
├── EDA.ipynb
├── best_model.pkl
├── requirements.txt
├── Dockerfile
├── .github/
│   └── workflows/
├── mlruns/
├── catboost_info/
├── dataset/
└── README.md
```

---

# 📊 Dataset

The dataset contains smartphone usage information collected from multiple users.

### Features include

- Age
- Gender
- Daily App Usage
- Number of Installed Applications
- Battery Drain
- Data Usage
- Sleep Hours
- Notifications Received
- Social Media Usage
- Gaming Time
- Study / Work Time
- Weekend Usage

Target:

- Estimated Daily Screen Time

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/AI-Powered-Mobile-Addiction-Risk-Prediction-System.git

cd AI-Powered-Mobile-Addiction-Risk-Prediction-System
```

Create virtual environment

```bash
python -m venv .venv
```

Activate environment

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the API

```bash
uvicorn app:app --reload
```

Open

```
http://127.0.0.1:8000/docs
```

to access the interactive Swagger UI.

---

# 🔄 Project Workflow

```text
Raw Dataset
      │
      ▼
Data Cleaning
      │
      ▼
Feature Engineering
      │
      ▼
Exploratory Data Analysis
      │
      ▼
Model Training
      │
      ▼
Model Evaluation
      │
      ▼
MLflow Tracking
      │
      ▼
Best Model Selection
      │
      ▼
FastAPI Deployment
      │
      ▼
Docker Container
      │
      ▼
Production API
```

---

# 📈 Feature Engineering

The project creates additional behavioral indicators including:

- Data Usage Per Hour
- Battery Drain Per Hour
- Device Stress Score
- Heavy Gamer Indicator
- Weekend Usage Behavior

These engineered features improve predictive performance by capturing user behavior more effectively.

---

# 🤖 Machine Learning Models

Multiple regression algorithms were evaluated during experimentation, including:

- Linear Regression
- Random Forest
- XGBoost
- LightGBM
- CatBoost

The best-performing model was selected based on evaluation metrics and deployed for inference.

---

# 📊 API Output

Example prediction response

```json
{
    "predicted_screen_time": 8.7,
    "risk_level": "High Addiction Risk",
    "recommendation": "Consider digital detox strategies and healthier usage patterns."
}
```

---

# 📉 Model Evaluation

The project evaluates models using appropriate regression metrics such as:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

Model comparison and experiment history are tracked using MLflow.

---

# 📦 Docker Support

Build Docker image

```bash
docker build -t mobile-addiction-api .
```

Run container

```bash
docker run -p 8000:8000 mobile-addiction-api
```

---

# 🚀 CI/CD Pipeline

The repository includes a GitHub Actions workflow that automates:

- Dependency installation
- Environment setup
- Project validation
- Continuous Integration
- Continuous Deployment readiness

---

# 💼 Business Applications

This solution can be integrated into:

- Digital Wellness Platforms
- Healthcare Applications
- EdTech Systems
- Employee Productivity Solutions
- Parental Control Applications
- Smartphone Analytics Platforms

---

# 📚 Skills Demonstrated

- Machine Learning
- Feature Engineering
- Data Preprocessing
- Exploratory Data Analysis
- Model Evaluation
- Experiment Tracking
- REST API Development
- FastAPI
- Docker
- MLflow
- GitHub Actions
- CI/CD
- Production Deployment

---

# 🔮 Future Improvements

- Deep Learning-based prediction
- Real-time user monitoring
- Mobile application integration
- Cloud deployment (AWS/Azure/GCP)
- User authentication and security
- Dashboard for usage analytics
- Explainable AI using SHAP/LIME

---

# 🤝 Contributing

Contributions are welcome.

Feel free to fork the repository, create a feature branch, and submit a pull request.

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Farsan K**

Data Scientist | Machine Learning Engineer

- 💼 LinkedIn: https://www.linkedin.com/in/farsank/
- 🌐 GitHub: https://github.com/Farsan-k
