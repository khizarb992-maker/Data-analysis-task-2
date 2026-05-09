# -*- coding: utf-8 -*-
"""
Created on Thu May  7 16:07:44 2026

@author: Khizar
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    confusion_matrix,
    classification_report,
    accuracy_score,
    roc_curve,
    roc_auc_score,
    f1_score,
)
import shap
df = pd.read_csv(r"E:\cleaned_bank_marketing_dataset.csv")
 
print(df.head())
print(df.info())
print(df.describe())
print("\nMissing values:\n", df.isnull().sum())
print("\nTarget distribution:\n", df["y"].value_counts())

sns.countplot(x="y", data=df)
plt.title("Term Deposit Subscription")
plt.tight_layout()
plt.show()

for col in df.select_dtypes(include="object").columns:
    df[col] = LabelEncoder().fit_transform(df[col])
    
X = df.drop("y", axis=1)
y = df["y"]
 
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

lr = LogisticRegression(max_iter=1000)
lr.fit(X_train_scaled, y_train)
y_pred_lr = lr.predict(X_test_scaled)

rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)

print(classification_report(y_test, y_pred_lr))
print("Accuracy :", accuracy_score(y_test, y_pred_lr))
print("F1 Score :", f1_score(y_test, y_pred_lr))
 
cm_lr = confusion_matrix(y_test, y_pred_lr)
sns.heatmap(cm_lr, annot=True, fmt="d", cmap="Blues")
plt.title("Logistic Regression – Confusion Matrix")
plt.tight_layout()
plt.show()

print(classification_report(y_test, y_pred_rf))
print("Accuracy :", accuracy_score(y_test, y_pred_rf))
print("F1 Score :", f1_score(y_test, y_pred_rf))
 
cm_rf = confusion_matrix(y_test, y_pred_rf)
sns.heatmap(cm_rf, annot=True, fmt="d", cmap="Greens")
plt.title("Random Forest – Confusion Matrix")
plt.tight_layout()
plt.show()

y_prob_lr = lr.predict_proba(X_test_scaled)[:, 1]
fpr_lr, tpr_lr, _ = roc_curve(y_test, y_prob_lr)
auc_lr = roc_auc_score(y_test, y_prob_lr)
 
y_prob_rf = rf.predict_proba(X_test)[:, 1]
fpr_rf, tpr_rf, _ = roc_curve(y_test, y_prob_rf)
auc_rf = roc_auc_score(y_test, y_prob_rf)
 
plt.figure(figsize=(8, 6))
plt.plot(fpr_lr, tpr_lr, label=f"Logistic Regression  AUC = {auc_lr:.2f}")
plt.plot(fpr_rf, tpr_rf, label=f"Random Forest        AUC = {auc_rf:.2f}")
plt.plot([0, 1], [0, 1], linestyle="--", color="grey")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.legend()
plt.tight_layout()
plt.show()

explainer = shap.TreeExplainer(rf)
shap_values = explainer.shap_values(X_test)

if isinstance(shap_values, list):
    sv_class1 = shap_values[1]
    ev_class1 = explainer.expected_value[1]

else:
    sv_class1 = shap_values[:, :, 1]
    ev_class1 = (
        explainer.expected_value[1]
        if hasattr(explainer.expected_value, "__len__")
        else explainer.expected_value
    )

for i in range(5):
    print(f"\nPrediction {i}  –  predicted class: {y_pred_rf[i]}")
    shap.force_plot(
        ev_class1,
        sv_class1[i],
        X_test.iloc[i],
        matplotlib=True,
        show=False,        
    )
    plt.title(f"SHAP Force Plot – sample {i}")
    plt.tight_layout()
    plt.show()   
    plt.close()

shap.summary_plot(sv_class1, X_test, show=False)
plt.tight_layout()
plt.show()









































