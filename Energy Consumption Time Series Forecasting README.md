# ⚡ Energy Consumption Time Series Forecasting

Forecast short-term household energy usage using historical electricity consumption data and compare multiple forecasting models including ARIMA, Prophet, and XGBoost.

---

# 📌 Project Objective

The goal of this project is to analyze household power consumption patterns and predict future energy usage using time series forecasting techniques.

The project focuses on:

- Time series preprocessing
- Feature engineering
- Forecasting model development
- Model comparison using evaluation metrics
- Visualization of predictions

---

# 📂 Dataset

Dataset Used:
Household Power Consumption Dataset

Source:
https://archive.ics.uci.edu/ml/datasets/individual+household+electric+power+consumption

The dataset contains:
- Date and Time
- Global Active Power
- Voltage
- Global Intensity
- Energy sub-metering values

---

# 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Statsmodels
- Prophet
- XGBoost

---

# 📊 Project Workflow

## 1. Data Preprocessing

- Parsed date and time columns
- Converted features to numeric format
- Removed missing values
- Set datetime index

---

## 2. Time Series Resampling

The raw data was resampled into hourly intervals for smoother forecasting and trend analysis.

---

## 3. Feature Engineering

Created time-based features such as:

- Hour of day
- Day
- Month
- Weekday
- Weekend indicator

Lag features were also added:
- Previous hour consumption
- Previous 24-hour consumption

---

# 🤖 Models Implemented

## 1. ARIMA

Statistical time series forecasting model used for capturing temporal dependencies.

### Strengths
- Good for linear patterns
- Handles autocorrelation well

---

## 2. Prophet

Forecasting library developed by Meta for handling seasonality and trends.

### Strengths
- Handles seasonality automatically
- Robust to missing data

---

## 3. XGBoost

Machine learning regression model trained using engineered time-based features.

### Strengths
- High predictive performance
- Handles nonlinear relationships effectively

---

# 📈 Model Evaluation

Models were evaluated using:

## MAE (Mean Absolute Error)

Measures average prediction error.

## RMSE (Root Mean Squared Error)

Measures error magnitude while penalizing larger errors.

---

# 📉 Visualization

The project includes:

- Actual vs Forecasted Energy Consumption Plot
- Comparative forecasting visualization
- Temporal trend analysis

---

# 📷 Sample Output

- Forecasted hourly energy usage
- Comparison of ARIMA, Prophet, and XGBoost predictions
- Error metric comparison
---

# 🎯 Skills Gained

- Time Series Forecasting
- Data Preprocessing
- Feature Engineering
- Machine Learning
- Statistical Modeling
- Forecast Visualization
- Model Evaluation

---


# 📚 Conclusion

This project demonstrates how different forecasting approaches perform on household energy consumption data.

- ARIMA captures statistical temporal patterns
- Prophet models seasonality effectively
- XGBoost leverages engineered features for strong predictive performance

The comparison provides valuable insights into selecting suitable forecasting techniques for energy analytics applications.

