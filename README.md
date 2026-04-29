# 🏠 House Price Prediction ML Project

An end-to-end Machine Learning project that predicts house prices based on key features like area, number of bedrooms, and bathrooms. The project includes data preprocessing, model training, evaluation, and a simple web application for real-time predictions.

---

## 🚀 Features

* 📊 Data preprocessing and cleaning
* 🤖 Machine Learning model using Random Forest
* 📈 Model evaluation using R² Score and RMSE
* 🌐 Interactive web app for predictions
* 💾 Model saving and reuse using joblib

---

## 🧠 Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* Joblib
* Streamlit

---

## 📁 Project Structure

```
house-price-ml/
│
├── data/
│   └── housing.csv          # Dataset
├── train.py                 # Model training script
├── app.py                   # Streamlit web app
├── model.pkl                # Saved trained model
├── requirements.txt         # Dependencies
└── README.md                # Project documentation
```

---

## 📊 How It Works

1. Load dataset and clean missing values
2. Split data into training and testing sets
3. Train a Random Forest regression model
4. Evaluate performance using R² Score & RMSE
5. Save trained model for future use
6. Deploy a web interface using Streamlit

---

## ▶️ Installation & Setup

### 1. Clone the repository

```
git clone <your-repo-link>
cd house-price-ml
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Train the model

```
python train.py
```

### 4. Run the web app

```
streamlit run app.py
```

---

## 🌐 Web App Preview

The web app allows users to input:

* Area (sq ft)
* Number of bedrooms
* Number of bathrooms

It then predicts the estimated house price instantly.

---

## 📈 Model Performance

* Algorithm: Random Forest Regressor
* Evaluation Metrics:

  * R² Score
  * RMSE (Root Mean Squared Error)

(*Note: Metrics may vary depending on dataset used*)

---

## 🔥 Future Improvements

* Use advanced models like XGBoost
* Add more features (location, amenities)
* Hyperparameter tuning (GridSearchCV)
* Deploy on cloud (AWS / Render)
* Improve UI/UX

---

## 📌 Use Case

This project can be used in:

* Real estate analytics
* Property price estimation tools
* ML portfolio projects

---

## 🙌 Author

Developed by Vinit Borawake

---

## ⭐ If you like this project

Give it a star ⭐ on GitHub and share it!
