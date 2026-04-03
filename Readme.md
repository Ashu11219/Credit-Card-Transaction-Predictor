# 📊 Credit Card Monthly Expense Predictor

## 🧠 Overview

This project focuses on predicting **monthly credit card spending** using historical transaction data.
The goal is not just to build a model, but to follow a **structured machine learning pipeline** — from raw data to final evaluation & compare Linear Regression and Random Forest Rregressor model for the given data.

---

## 📊 Results

| Metric                                    | Value |
|-------------------------------------------|------|
| Best Model                                | Random Forest Regressor |
| Validation Mean Absolute Percentage Error | 2.95% |
| Test Mean Absolute Error                  | 1,433,415.73 |
| Test Mean Absolute Percentage Error    | 7.89% |

---

## 🎯 Problem Definition

> Predict the total amount of money that will be spent in a given month based on past transaction data.

---

## 📥 Data Collection

* Dataset sourced from Kaggle
* Contains transaction-level credit card data (India-based)

---

## 🧹 Data Cleaning

The raw dataset was preprocessed to ensure consistency and usability:

* Converted date columns into proper datetime format
* Cleaned numerical fields (amounts)
* Removed redundant information (e.g., constant values like country)
* Checked and handled missing values
* Removed duplicates (if any)

---

## 🔍 Exploratory Data Analysis (EDA)

Performed EDA to understand the nature of the data:

* Visualized monthly spending trends
* Observed fluctuations and patterns in expenses
* Checked for correlations and anomalies
* Identified that the data does **not follow a clear linear trend**

---

## ⚙️ Feature Engineering

* Aggregated transaction-level data into **monthly totals**
* Created numerical representation of time (`month_num`)
* Prepared dataset in a format suitable for machine learning models

---

## ✂️ Data Splitting

Data was split **chronologically** (important for time-based data):

* **Training set** → model learns patterns
* **Validation set** → model selection and tuning
* **Test set** → final evaluation

---

## 🤖 Model Selection

* Implemented **Linear Regression** as a baseline model
* Compared with other approaches (e.g., Random Forest)

---

## 🏋️ Model Training

* Models were trained on the training dataset
* Learned parameters based on historical spending patterns

---

## 📏 Evaluation

Models were evaluated using:

* **MAE (Mean Absolute Error)** → absolute difference
* **MAPE (Mean Absolute Percentage Error)** → percentage-based error

Evaluation was performed on:

* Validation set (for comparison)
* Test set (for final performance)

---

## 🔁 Iteration

Based on evaluation:

* Model assumptions were analyzed
* Linear regression limitations were identified
* Alternative models were explored

---


## 🧱 Project Structure

```
project/
│
├── preprocess.py              # Data cleaning & transformation
├── exploratory_data_analysis.py  # EDA + data splitting
├── model.py                  # Model training & evaluation
├── main.py                   # Execution pipeline
├── data/                     # Dataset
└── README.md
```

---

## 🚀 Key Takeaways

* Machine learning is not just about models, but about **data understanding and decision-making**
* Proper data splitting is crucial for time-based problems
* Simpler models help in understanding assumptions before moving to complex ones

---

## 📌 Future Improvements

* Use larger datasets for better generalization
* Add more features (lag values, rolling averages, seasonality)
* Improve model performance with advanced techniques
* Deploy model as an API and integrate into a full-stack application

---

## 💡 Final Note

This project emphasizes **thinking over tooling** — focusing on understanding data, questioning assumptions, and making informed model choices.
