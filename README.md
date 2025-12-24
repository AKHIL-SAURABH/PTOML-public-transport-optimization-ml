# 🚍 Public Transport Optimization using Machine Learning (Mini Project)

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-green)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-success)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![Status](https://img.shields.io/badge/Project-Completed-brightgreen)

---

## 📌 Project Overview

Public transport systems often suffer from **unpredictable arrival times** and **overcrowding**, resulting in commuter dissatisfaction, operational inefficiencies, and increased reliance on private vehicles.

This mini project presents an **end-to-end Machine Learning–based system** that predicts:

- ⏱️ **Bus Arrival Time (ETA)**
- 👥 **Crowding Level**

The project demonstrates how **data-driven intelligence** can transform traditional public transport systems into **predictive and decision-support systems**.

---

## ❓ Problem Statement

- Static bus schedules fail during traffic congestion and peak hours  
- Commuters lack real-time arrival and crowding information  
- Transport authorities do not have predictive insights for planning  
- Overcrowding reduces passenger comfort and service reliability  

---

## 💡 Proposed Solution

This project builds a machine learning system that:

- Learns transport patterns from historical data  
- Predicts **ETA** using time, route, traffic, and weather features  
- Predicts **crowding level** using passenger occupancy  
- Exposes predictions via a **FastAPI REST API**  
- Visualizes predictions using a **Streamlit dashboard**

---

## 🏗️ System Architecture

```
Synthetic Transport Data
↓
Feature Engineering
↓
Machine Learning Models
↓
FastAPI Backend
↓
Streamlit Dashboard

```
---

## 📊 Features Implemented

### ✅ ETA Prediction (Regression)
Predicts the estimated travel time (in minutes) to the next bus stop.

### ✅ Crowding Prediction (Classification)
Classifies crowding into:
- Low
- Medium
- High

### ✅ REST API
A FastAPI backend exposes a `/predict` endpoint for real-time inference.

### ✅ Interactive Dashboard
A Streamlit dashboard allows users to simulate different transport conditions and view live predictions.

---

## 🧠 Machine Learning Models Used

| Task | Model |
|----|------|
| ETA Prediction | Random Forest Regressor |
| Crowding Prediction | Random Forest Classifier |

---

## 📈 Model Performance (Synthetic Data)

- **ETA Mean Absolute Error (MAE):** ≈ **0.43 minutes**
- **Crowding Classification Accuracy:** ≈ **100%**

> ⚠️ Note:  
> These results are obtained on **controlled synthetic data**.  
> Real-world performance depends on live data quality, noise, and sensor availability.

---

## 🧾 Input Factors Used for Prediction (Dashboard Controls)

The Streamlit dashboard allows users to configure the following inputs:

| Factor | Description | Effect on Prediction |
|------|------------|---------------------|
| Hour | Time of day (0–23) | Peak hours increase ETA & crowding |
| Day of Week | 0 (Mon) – 6 (Sun) | Weekdays show higher congestion |
| Is Weekend | Binary flag | Reduces commute-based traffic |
| Route ID | Bus route identifier | Captures route-specific delays |
| Stop Sequence | Position in route | Higher stop number → cumulative delay |
| Distance to Next Stop (km) | Physical distance | Longer distance → higher ETA |
| Traffic Level | 1 (Low) – 3 (High) | Strongest contributor to delay |
| Rain Flag | Weather condition | Rain increases travel time |
| Passenger Count | Current passengers | Determines crowding |
| Bus Capacity | Maximum capacity | Normalizes crowding |

Users can adjust these values to simulate **real-world transport scenarios**.

---

## 🔍 What the Results Tell Us

- Travel time strongly depends on **time of day**, **traffic**, and **weather**
- Peak hours consistently produce higher ETA and crowding
- Normalized passenger load effectively captures crowding conditions
- Machine learning predictions outperform static schedules

This validates the effectiveness of **ML-driven transport optimization**.

---

## 🖥️ Screenshots

### SWAGGER UI BACKEND:
![SWAGGER](https://github.com/AKHIL-SAURABH/PTOML-public-transport-optimization-ml/blob/main/screenshots/Screenshot_24-12-2025_163253_127.0.0.1.jpeg)

---
### HIGH CROWD LEVEL WITH ETA:
![HIGH](https://github.com/AKHIL-SAURABH/PTOML-public-transport-optimization-ml/blob/main/screenshots/high.jpg)

---
### LOW CROWD LEVEL WITH ETA:
![HIGH](https://github.com/AKHIL-SAURABH/PTOML-public-transport-optimization-ml/blob/main/screenshots/low.jpg)

---
### MWDIUM CROWD LEVEL WITH ETA:
![HIGH](https://github.com/AKHIL-SAURABH/PTOML-public-transport-optimization-ml/blob/main/screenshots/medium.jpg)

---

## ▶️ How to Run This Project Locally

### ⚠️ Important Note on Model Files

Trained model files (`.pkl`) are **NOT uploaded to GitHub** due to GitHub file size limits and best practices.

Anyone can recreate them locally by following the steps below.

---

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/AKHIL-SAURABH/PTOML-public-transport-optimization-ml.git
cd PTOML-public-transport-optimization-ml

```
---

### 2️⃣ Create & Activate Virtual Environment

```bash
python -m venv venv
```

**Windows**

```bash
venv\Scripts\activate
```

**Linux / Mac**

```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Generate Data & Train Models

Run the notebooks **in order**:

```
notebooks/01_data_generation.ipynb
notebooks/03_model_training.ipynb
```

This will generate all required `.pkl` model files locally.

---

### 5️⃣ Start FastAPI Backend

```bash
uvicorn app.main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

### 6️⃣ Run Streamlit Dashboard

Open a new terminal (with venv activated):

```bash
streamlit run dashboard/dashboard.py
```

The dashboard will open automatically in your browser.

---

## 🛠️ Tech Stack

* **Programming Language:** Python
* **Data Processing:** Pandas, NumPy
* **Machine Learning:** Scikit-learn
* **Backend API:** FastAPI
* **Dashboard:** Streamlit
* **Version Control:** Git & GitHub

---

## 🎯 Project Type

* Mini Project
* End-to-End Machine Learning System
* Portfolio / Resume Ready
* Demonstrates ML → API → UI workflow

---

## 👤 Author

**Akhil Saurabh**
Computer Science | Data Science & Machine Learning Enthusiast

---

## 📌 Conclusion

This project demonstrates how **machine learning can transform reactive public transport systems into predictive systems**, enabling better planning, improved commuter experience, and data-driven decision-making.

```

