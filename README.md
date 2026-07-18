# 🦟 MalariaGuard AI

An AI-powered malaria prediction and early warning system that uses **Random Forest Machine Learning** and **weather parameters** to forecast district-level malaria cases. The application provides an interactive dashboard for malaria surveillance and risk assessment.

---

## 🚀 Features

- 🧠 Random Forest-based malaria prediction
- 📍 District-wise disease forecasting
- 🌦 Weather parameter analysis (Temperature, Humidity, Rainfall)
- 📊 Interactive dashboard built with Streamlit
- 🚨 AI-generated malaria risk assessment
- 📈 Data visualization using Plotly

---

## 🖥️ Application Workflow

```
Home
   ↓
Select District
   ↓
AI Prediction Engine
   ↓
Prediction Dashboard
```

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Plotly
- Joblib

---

## 📂 Project Structure

```
MalariaGuard-AI/
│
├── app.py
├── backend.py
├── data_engine.py
├── prediction.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── pages/
│   ├── Location.py
│   ├── Processing.py
│   └── Dashboard.py
```

---

## 📸 Screenshots

### 🏠 Home Page

> Add `screenshots/home.png`

### 📍 District Selection

> Add `screenshots/location.png`

### 🤖 AI Prediction

> Add `screenshots/processing.png`

### 📊 Dashboard

> Add `screenshots/dashboard.png`

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/Prasanth4734f/MalariaGuard-AI.git
```

Move into the project directory

```bash
cd MalariaGuard-AI
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 📊 Machine Learning Model

- Algorithm: Random Forest Classifier
- Input Features:
  - Temperature
  - Humidity
  - Rainfall
  - Historical Malaria Trends
- Output:
  - Predicted Malaria Cases
  - Risk Level

---

## 🎯 Future Scope

- Support all districts of Andhra Pradesh
- Real-time weather API integration
- GIS-based malaria hotspot mapping
- Deep Learning-based prediction models
- Mobile application integration
- Public health notification system

---

## 👨‍💻 Author

**M. Prasanth Reddy**

GitHub: https://github.com/Prasanth4734f

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.