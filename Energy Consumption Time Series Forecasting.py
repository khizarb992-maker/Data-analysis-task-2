# -*- coding: utf-8 -*-
"""
Created on Sat May 16 11:30:22 2026

@author: Khizar
"""

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split

from statsmodels.tsa.arima.model import ARIMA
from prophet import Prophet
from xgboost import XGBRegressor

df = pd.read_csv(
    r"E:\household_power_consumption.txt",
    sep=';',
    parse_dates={'datetime': ['Date', 'Time']},
    infer_datetime_format=True,
    na_values=['?'],
    low_memory=False
)

print(df.head())

cols = [
    'Global_active_power',
    'Global_reactive_power',
    'Voltage',
    'Global_intensity',
    'Sub_metering_1',
    'Sub_metering_2',
    'Sub_metering_3'
]

for col in cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')
    
df = df.dropna() 

df.set_index('datetime', inplace=True)

hourly_df = df.resample('H').mean()

hourly_df = hourly_df[['Global_active_power']]
hourly_df.dropna(inplace=True)


hourly_df['hour'] = hourly_df.index.hour
hourly_df['day'] = hourly_df.index.day
hourly_df['month'] = hourly_df.index.month
hourly_df['weekday'] = hourly_df.index.weekday

hourly_df['is_weekend'] = hourly_df['weekday'].isin([5,6]).astype(int)

hourly_df['lag_1'] = hourly_df['Global_active_power'].shift(1)
hourly_df['lag_24'] = hourly_df['Global_active_power'].shift(24)

hourly_df.dropna(inplace=True)


train_size = int(len(hourly_df) * 0.8)

train = hourly_df[:train_size]
test = hourly_df[train_size:]

arima_model = ARIMA(
    train['Global_active_power'],
    order=(5,1,2)
)

arima_fit = arima_model.fit()

arima_forecast = arima_fit.forecast(
    steps=len(test)
)


prophet_df = train.reset_index()[['datetime', 'Global_active_power']]
prophet_df.columns = ['ds', 'y']

prophet_model = Prophet()

prophet_model.fit(prophet_df)

future = prophet_model.make_future_dataframe(
    periods=len(test),
    freq='H'
)

forecast = prophet_model.predict(future)

prophet_forecast = forecast['yhat'][-len(test):].values

features = [
    'hour',
    'day',
    'month',
    'weekday',
    'is_weekend',
    'lag_1',
    'lag_24'
]

X_train = train[features]
y_train = train['Global_active_power']

X_test = test[features]
y_test = test['Global_active_power']

xgb_model = XGBRegressor(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=6,
    random_state=42
)

xgb_model.fit(X_train, y_train)

xgb_forecast = xgb_model.predict(X_test)

def evaluate_model(name, actual, predicted):
    mae = mean_absolute_error(actual, predicted)
    rmse = np.sqrt(mean_squared_error(actual, predicted))

    print(f"{name}")
    print(f"MAE: {mae:.4f}")
    print(f"RMSE: {rmse:.4f}")
    print("-"*30)

evaluate_model(
    "ARIMA",
    test['Global_active_power'],
    arima_forecast
)

evaluate_model(
    "Prophet",
    test['Global_active_power'],
    prophet_forecast
)

evaluate_model(
    "XGBoost",
    y_test,
    xgb_forecast
)

plt.figure(figsize=(15,6))

plt.plot(
    test.index,
    test['Global_active_power'],
    label='Actual',
    linewidth=2
)

plt.plot(
    test.index,
    arima_forecast,
    label='ARIMA Forecast'
)

plt.plot(
    test.index,
    prophet_forecast,
    label='Prophet Forecast'
)

plt.plot(
    test.index,
    xgb_forecast,
    label='XGBoost Forecast'
)

plt.title("Energy Consumption Forecasting")
plt.xlabel("Time")
plt.ylabel("Global Active Power")
plt.legend()

plt.show()













