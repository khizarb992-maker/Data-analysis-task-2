# 📊 Term Deposit Subscription Prediction

## 📌 Project Overview

This project predicts whether a bank customer will subscribe to a term deposit based on marketing campaign data.  
The dataset comes from the UCI Machine Learning Repository Bank Marketing Dataset.

The project includes:

- Data Cleaning
- Feature Encoding
- Classification Models
- Model Evaluation
- Explainable AI using SHAP

---

# 🎯 Objective

The objective of this project is to build machine learning models that can predict customer subscription behavior for term deposits.

This helps banks:

- Improve marketing strategies
- Identify potential customers
- Reduce unnecessary marketing costs
- Increase campaign efficiency

---

# 🗂 Dataset Information

Dataset: Bank Marketing Dataset

Target Variable:

```python
y
```

- `yes` → Customer subscribed
- `no` → Customer did not subscribe

---

# 📁 Project Structure

```text
Term-Deposit-Prediction/
│
├── data/
│   ├── bank-additional-full.csv
│   └── cleaned_bank_marketing_dataset.csv
│
├── notebooks/
│   └── analysis.ipynb
│
├── models/
│
├── visuals/
│
├── README.md
│
└── requirements.txt
```

---

# ⚙️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- SHAP

---

# 🧹 Data Cleaning

The following preprocessing steps were performed:

- Removed duplicate rows
- Handled missing values
- Replaced `"unknown"` values
- Cleaned column names
- Encoded categorical features

---

# 📊 Features Used

```text
age
job
marital
education
default
housing
loan
contact
month
day_of_week
duration
campaign
pdays
previous
poutcome
emp.var.rate
cons.price.idx
cons.conf.idx
euribor3m
nr.employed
```

Target column:

```text
y
```

---

# 🤖 Machine Learning Models

The following classification models were trained:

## 1️⃣ Logistic Regression

Used for baseline binary classification.

## 2️⃣ Random Forest Classifier

Used for improved prediction performance and feature importance analysis.

---

# 📈 Model Evaluation

The models were evaluated using:

- Confusion Matrix
- Accuracy Score
- F1 Score
- ROC Curve
- Classification Report

---

# 🔍 Explainable AI (XAI)

SHAP (SHapley Additive Explanations) was used to explain model predictions.

The project includes:

- SHAP Summary Plot
- Feature Importance
- Individual Prediction Explanations

---

# 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/term-deposit-prediction.git
```

Move into the project folder:

```bash
cd term-deposit-prediction
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Project

Run the Python script:

```bash
python main.py
```

Or open Jupyter Notebook:

```bash
jupyter notebook
```

---

# 📦 Required Libraries

```bash
pip install pandas numpy matplotlib seaborn scikit-learn shap
```

---

# 📉 Sample Workflow

1. Load Dataset
2. Clean Data
3. Encode Features
4. Split Dataset
5. Train Models
6. Evaluate Performance
7. Explain Predictions using SHAP

---

# 📌 Results

- Random Forest performed better than Logistic Regression
- SHAP helped identify important customer behavior patterns
- Features like duration, month, and contact type strongly influenced predictions

---

# 📚 Skills Gained

- Data Preprocessing
- Feature Engineering
- Classification Modeling
- Model Evaluation
- Explainable AI (XAI)
- Customer Behavior Analysis

---

# 🔮 Future Improvements

Possible future enhancements:

- Hyperparameter Tuning
- XGBoost / LightGBM
- Streamlit Dashboard
- SMOTE for Class Imbalance
- Deployment using FastAPI

---

# 👨‍💻 Author

MKB 16

---

# ⭐ Conclusion

This project demonstrates how machine learning can help banks predict customer subscription behavior and improve marketing campaign effectiveness.

The combination of predictive modeling and explainable AI provides both accuracy and interpretability for business decision-making.
