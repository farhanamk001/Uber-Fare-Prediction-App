# 🚕 Uber Fare Prediction using Machine Learning

## 📌 Project Description
This project predicts **Uber ride fares (in USD)** based on pickup and drop-off locations, date & time, passenger count, and travel distance.  
A **Random Forest Regressor** model is trained on historical Uber trip data and deployed as an **interactive Streamlit web application** for real-time predictions.

The project demonstrates the **end-to-end machine learning workflow** including data preprocessing, feature engineering, model training, evaluation, and deployment.

---

## 🎯 Objectives
- Analyze Uber trip data
- Perform feature engineering on datetime and location data
- Train a machine learning regression model
- Evaluate model performance
- Deploy the model using Streamlit for real-time predictions

---

## 🛠️ Technologies Used
- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  
- Scikit-learn  
- Haversine  
- Streamlit  
- Joblib  

---
## 📊 Dataset
The dataset contains historical Uber trip records with the following features:
- Pickup latitude and longitude
- Dropoff latitude and longitude
- Pickup datetime
- Passenger count
- Fare amount (target variable)

---

## ⚙️ Feature Engineering
- Extracted features from pickup datetime:
  - Day
  - Month
  - Year
  - Day of week
  - Hour
- Calculated distance between pickup and dropoff locations using the **Haversine formula**
- Removed outliers and invalid latitude/longitude values
- Cleaned missing and zero-value records

---

## 🤖 Machine Learning Model
- Algorithm: **Random Forest Regressor**
- Reason: Handles non-linear relationships and noisy real-world data effectively
- Evaluation Metrics:
  - R² Score
  - Mean Squared Error (MSE)
  - Root Mean Squared Error (RMSE)

---

## 🌐 Streamlit Web Application
### Features:
- User-friendly input form
- Real-time fare prediction
- Distance validation
- Automatic input reset after prediction
- Output displayed in **USD**


