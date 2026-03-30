# 📊 Retail Sales Forecasting Dashboard

An end-to-end machine learning project that predicts retail store sales using advanced time-series modeling and an interactive web dashboard.

---

## 🚀 Project Overview

This project builds a **Retail Sales Forecasting System** using LightGBM and time-series feature engineering techniques such as lag features, rolling statistics, and promotion-based signals.

The trained model is deployed through an interactive Streamlit dashboard that allows users to input store and product details and receive real-time sales predictions.

---

## 🔗 Kaggle Notebook

👉 https://www.kaggle.com/code/tushardobal/time-series-sales-forecasting-with-lightgbm

---

## 🎯 Key Features

* 📈 Time-series forecasting using LightGBM
* 🔁 Recursive prediction pipeline
* 🧠 Advanced feature engineering (lags, rolling windows, promotions)
* 🌐 Interactive web app using Streamlit
* 🎨 Clean UI with animations and modern design
* ⚡ Fast predictions with real-time interaction

---

## 🧪 Model Details

* **Algorithm:** LightGBM Regressor
* **Target Transformation:** Log transformation (`log1p`)
* **Evaluation Metric:** RMSLE
* **Kaggle Score:** ~0.57 (Top ~15–20%)

### Feature Engineering:

* Lag features: 1, 7, 14, 28, 56, 112 days
* Rolling means: 7, 14, 28 days
* Promotion-based features
* Date features (day, month, weekday, weekend)
* External data: Oil prices

---

## 🛠️ Tech Stack

* Python
* Pandas & NumPy
* LightGBM
* Streamlit
* Scikit-learn

---

## ▶️ How to Run Locally

### 1. Clone the repository

```
git clone https://github.com/your-username/retail-sales-forecast.git
cd retail-sales-forecast
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Run the app

```
streamlit run app.py
```

---

## 🌐 Live Demo
👉 https://retail-sales-forecast-app.streamlit.app

---

## 📸 Screenshots

<img width="1920" height="966" alt="Screenshot 2026-03-30 162947" src="https://github.com/user-attachments/assets/e42155fa-6a69-4017-a14c-b9481a1e6d0b" />

---

## 💡 Future Improvements

* Add real historical data input for accurate lag features
* Integrate visualization dashboards
* Deploy using cloud services
* Add model explainability (SHAP)

---

## 👨‍💻 Author

**Tushar Dobal**
Aspiring Data Scientist | ML & AI Enthusiast

---

## ⭐ Acknowledgements

* Kaggle Store Sales Forecasting Competition
* Open-source ML community

---

## 📌 Conclusion

This project demonstrates how machine learning and time-series techniques can be applied to solve real-world retail forecasting problems, combining both predictive modeling and interactive deployment.
