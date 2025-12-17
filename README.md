# 🏠 California Housing Price Prediction

This project is an **end-to-end Machine Learning application** that predicts **median house prices in California** based on demographic, geographic, and housing-related features.  
The project includes **data preprocessing, model training, and deployment using Streamlit**.

---

## 📌 Project Overview

The goal of this project is to build a **regression model** that accurately predicts housing prices using features such as:
- Location (latitude & longitude)
- Number of rooms and bedrooms
- Population and households
- Median income
- Proximity to the ocean

An **interactive Streamlit dashboard** allows users to input values and receive real-time predictions.

---

## 🚀 Live Application

🔗 **Streamlit App:**  
https://housing-price-prediction-dyapphionvygjvy7ygelcjb.streamlit.app/

---

## 🧠 Machine Learning Workflow

### 1. Data Collection
- Dataset: **California Housing Dataset**
- Source: Kaggle / Scikit-learn

### 2. Data Preprocessing
- Handled missing values
- Encoded categorical features (`ocean_proximity`)
- Feature scaling using `StandardScaler`
- Train-test split

### 3. Model Development
- Algorithm: **Linear Regression**
- Pipeline used for scaling + model training
- Performance evaluated using R², MAE, and RMSE

### 4. Deployment
- Built interactive UI using **Streamlit**
- Implemented **auto-training logic** (model trains automatically if not found)
- Deployed on **Streamlit Cloud**

---

## 📂 Project Structure

housing-price-prediction/
│
├── app.py # Streamlit dashboard
├── train_model.py # Model training script
├── requirements.txt # Dependencies
├── README.md # Project documentation
│
├── data/
│ └── housing.csv # Dataset
│
├── model/
│ └── model.pkl # Trained model (auto-generated)

yaml
Copy code

---

## ⚙️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Joblib
- Git & GitHub

---

## ▶️ How to Run the Project Locally

### 1. Clone the Repository
```bash
git clone https://github.com/hassan-Khawaja-bot/housing-price-prediction.git
cd housing-price-prediction
2. Install Dependencies
bash
Copy code
pip install -r requirements.txt
3. Train the Model
bash
Copy code
python train_model.py
4. Run Streamlit App
bash
Copy code
streamlit run app.py
📈 Model Performance
R² Score: ~0.60

Mean Absolute Error (MAE): ~0.5

Root Mean Squared Error (RMSE): ~0.7

Note: This is a baseline model. Performance can be improved using Random Forest or Gradient Boosting.

📌 Key Features
✔ End-to-end ML pipeline
✔ Interactive dashboard
✔ Auto model training
✔ Cloud deployment
✔ Clean and modular code

🔮 Future Improvements
Use advanced models (Random Forest, XGBoost)

Add data visualizations and maps

Hyperparameter tuning

Feature importance analysis

👤 Author
Hassan Khawaja
GitHub: https://github.com/hassan-Khawaja-bot

Internship: ARCH Technologies

📄 License
This project is for educational and internship purposes.