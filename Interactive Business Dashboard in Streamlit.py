# -*- coding: utf-8 -*-
"""
Created on Sat May 16 12:13:49 2026

@author: Khizar
"""

import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------------
# PAGE CONFIG
# ---------------------------
st.set_page_config(page_title="Superstore Dashboard", layout="wide")
st.title("📊 Global Superstore Business Dashboard")

# ---------------------------
# LOAD DATA
# ---------------------------
df = pd.read_csv(r"E:\superstore.csv", encoding="latin1")

# ---------------------------
# CLEANING
# ---------------------------
df = df.dropna(subset=["Sales", "Profit"])

# Ensure correct types
df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")
df["Profit"] = pd.to_numeric(df["Profit"], errors="coerce")

# ---------------------------
# SIDEBAR FILTERS
# ---------------------------
st.sidebar.header("🔍 Filters")

region = st.sidebar.multiselect(
    "Select Region",
    df["Region"].unique(),
    default=df["Region"].unique()
)

category = st.sidebar.multiselect(
    "Select Category",
    df["Category"].unique(),
    default=df["Category"].unique()
)

# FIX 1: Renamed `sub.category` → `sub_category` (dots are invalid in variable names)
# FIX 2: Column name changed to "Sub-Category" — update this to match your actual CSV column name
sub_category = st.sidebar.multiselect(
    "Select Sub.Category",
    df["Sub.Category"].unique(),
    default=df["Sub.Category"].unique()
)

# ---------------------------
# FILTER DATA
# ---------------------------
filtered_df = df[
    (df["Region"].isin(region)) &
    (df["Category"].isin(category)) &
    (df["Sub.Category"].isin(sub_category))
]

# ---------------------------
# KPI METRICS
# ---------------------------
total_sales = filtered_df["Sales"].sum()
total_profit = filtered_df["Profit"].sum()

col1, col2 = st.columns(2)
col1.metric("💰 Total Sales", f"${total_sales:,.2f}")
col2.metric("📈 Total Profit", f"${total_profit:,.2f}")

# ---------------------------
# TOP CUSTOMERS
# ---------------------------
st.subheader("🏆 Top 5 Customers by Sales")
top_customers = (
    filtered_df.groupby("Customer.Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
    .reset_index()
)
fig1 = px.bar(
    top_customers,
    x="Customer.Name",
    y="Sales",
    title="Top 5 Customers"
)
st.plotly_chart(fig1, use_container_width=True)

# ---------------------------
# SALES BY CATEGORY
# ---------------------------
st.subheader("📦 Sales by Category")
cat_sales = filtered_df.groupby("Category")["Sales"].sum().reset_index()
fig2 = px.pie(
    cat_sales,
    names="Category",
    values="Sales",
    title="Category-wise Sales Distribution"
)
st.plotly_chart(fig2, use_container_width=True)

# ---------------------------
# SALES BY REGION
# ---------------------------
st.subheader("📉 Sales by Region")
region_sales = filtered_df.groupby("Region")["Sales"].sum().reset_index()
fig3 = px.bar(
    region_sales,
    x="Region",
    y="Sales",
    color="Region",
    title="Region-wise Sales"
)
st.plotly_chart(fig3, use_container_width=True)