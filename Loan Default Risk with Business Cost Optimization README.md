# 💳 Loan Default Risk with Business Cost Optimization

A machine learning project that predicts loan default risk and optimizes decision thresholds using business cost analysis instead of traditional accuracy metrics.

---

# 🎯 Objective

Build a binary classification system to predict loan defaults and optimize decision-making using a **cost-sensitive approach**, minimizing financial loss from:

- ❌ False Negatives (bad loans approved)
- ❌ False Positives (good customers rejected)

---

# 📂 Dataset

📌 Kaggle: Home Credit Default Risk  
https://www.kaggle.com/c/home-credit-default-risk

Main file used:
- `application_train.csv`

Target column:
- `TARGET` (1 = default, 0 = non-default)

---

# 🛠 Tech Stack

- Python 🐍
- Pandas
- NumPy
- Scikit-learn
- CatBoost
- Matplotlib

---

# 🔄 Workflow

## 1. Data Preprocessing
- Handle missing values
- Select numeric features
- Clean dataset for modeling

---

## 2. Train-Test Split
Split data into training and testing sets using stratified sampling.

---

## 3. Models Used

### 📌 Logistic Regression
- Baseline interpretable model

### 📌 CatBoost Classifier
- Handles complex relationships
- Strong performance on tabular data

---

## 4. Probability Prediction
Models output probability of default instead of direct labels.

---

## 5. Business Cost Function

Instead of accuracy, we define real-world financial impact:

- False Negative (FN): $10,000 loss
- False Positive (FP): $500 opportunity loss

---

## 6. Threshold Optimization

We test multiple probability thresholds (0.1 → 0.9) and select:

> 🎯 Threshold with minimum total business cost

---

## 7. Evaluation Metrics

- ROC-AUC Score
- Confusion Matrix
- Business Cost Score

---

## 8. Visualization

- Threshold vs Cost curve
- Model performance comparison

---

# 📊 Key Insight

Instead of asking:

> ❌ “How accurate is the model?”

We ask:

> 💡 “How much money does the model save?”

---

# 🚀 How to Run

## 1. Install dependencies

```bash
pip install pandas numpy scikit-learn matplotlib catboost

---

# 📈 Skills Learned

- Binary Classification
- Risk Modeling
- Cost-sensitive Machine Learning
- Threshold Optimization
- Feature Engineering
- Business-driven AI thinking

---



---

# 👨‍💻 Outcome

A real-world financial ML system that prioritizes **profit-aware decision making** over simple accuracy metrics.
