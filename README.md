# 🏠 Bengaluru House Price Prediction

This project aims to predict the prices of houses in Bengaluru using machine learning techniques. It includes data preprocessing, feature engineering, model training, and a deployed Streamlit app for interactive predictions.

---

# 📌 Table of Contents

- [Overview](#overview)
- [Dataset](#dataset)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [How to Run](#how-to-run)
- [Screenshots](#screenshots)

---

## 📖 Overview

The real estate market in Bengaluru is diverse and complex. This project attempts to:
- Clean and process the raw housing dataset.
- Train and evaluate multiple regression models.
- Provide an interactive web app for users to estimate house prices based on features like location, square footage, number of BHKs, and bathrooms.

---

## 📂 Dataset

- **Source**: Kaggle  
- **Name**: Bengaluru House Price Data  
- [View on Kaggle →](https://www.kaggle.com/datasets/amitabhajoy/bengaluru-house-price-data)

---

## ⚙️ Features

- 📊 Data cleaning, EDA, and visualization
- 🔎 Outlier detection and removal
- 🧠 Model building using Linear Regression
- 📈 Feature selection and transformation
- 🌐 Streamlit app for live price prediction
- 📁 Model saving using `pickle`

---

## 💻 Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core language |
| Pandas, NumPy | Data manipulation |
| Matplotlib, Seaborn | Visualization |
| Scikit-learn | ML modeling |
| Streamlit | Frontend web app |
| Git, GitHub | Version control and hosting |

---

## 🧾 Project Structure
```
bengaluru-house-price-prediction/
├── Bengaluru_House.ipynb
├── model/
│   └── model.pkl            ← Your trained model
├── streamlit_app/
│   └── app.py               ← Streamlit code
├── data/
│  └── datacolumns.json         ← Column names (for one-hot encoding)
├──requirements.txt
```


---

## 🚀 How to Run Locally

1. **Clone the repository**:

```bash
git clone https://github.com/sumukhpshetty25/bengaluru-house-price-prediction.git
cd bengaluru-house-price-prediction
```
2. **Install dependencies**:
```bash
pip install -r requirements.txt
```
3. **Run the Streamlit app**:
```bash
cd streamlit_app
streamlit run app.py
```

---

## Screenshots
<img width="1309" height="785" alt="Image" src="https://github.com/user-attachments/assets/b1e8c337-01b8-49cb-a590-3761c9c874b8" />

<img width="1340" height="862" alt="Image" src="https://github.com/user-attachments/assets/33050fa9-1c44-4a4e-ab1a-033e714e3dc3" />
