# -*- coding: utf-8 -*-
"""
Created on Sat May 16 11:53:53 2026

@author: Khizar
"""

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, confusion_matrix

from catboost import CatBoostClassifier

import matplotlib.pyplot as plt

df = pd.read_csv(r"E:\application_train.csv")

print(df.shape)
print(df.head())

# Target
y = df["TARGET"]
X = df.drop(columns=["TARGET"])

# Keep only numeric for simplicity (you can expand later)
X = X.select_dtypes(include=[np.number])

# Impute missing values
imputer = SimpleImputer(strategy="median")
X = pd.DataFrame(imputer.fit_transform(X), columns=X.columns)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

log_model = LogisticRegression(max_iter=1000)
log_model.fit(X_train, y_train)

log_probs = log_model.predict_proba(X_test)[:, 1]
cat_model = CatBoostClassifier(
    iterations=200,
    learning_rate=0.1,
    depth=6,
    verbose=0
)

cat_model.fit(X_train, y_train)

cat_probs = cat_model.predict_proba(X_test)[:, 1]

FN_COST = 10000
FP_COST = 500
def calculate_cost(y_true, y_pred, threshold):
    preds = (y_pred >= threshold).astype(int)

    tn, fp, fn, tp = confusion_matrix(y_true, preds).ravel()

    cost = (fn * FN_COST) + (fp * FP_COST)
    return cost
thresholds = np.arange(0.1, 0.9, 0.01)

best_threshold = 0
best_cost = float("inf")

for t in thresholds:
    cost = calculate_cost(y_test, cat_probs, t)

    if cost < best_cost:
        best_cost = cost
        best_threshold = t

print("Best Threshold:", best_threshold)
print("Minimum Business Cost:", best_cost)
final_preds = (cat_probs >= best_threshold).astype(int)

print("ROC-AUC:", roc_auc_score(y_test, cat_probs))
print("Confusion Matrix:")
print(confusion_matrix(y_test, final_preds))
costs = []

for t in thresholds:
    costs.append(calculate_cost(y_test, cat_probs, t))

plt.plot(thresholds, costs)
plt.xlabel("Threshold")
plt.ylabel("Business Cost")
plt.title("Threshold Optimization Curve")
plt.show()