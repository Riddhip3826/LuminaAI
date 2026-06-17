# Lumina AI

AI-powered ecommerce revenue forecasting and marketing intelligence platform.

## Overview

Lumina AI helps ecommerce businesses analyze marketing performance, forecast future revenue, identify risks, and optimize advertising spend across multiple channels.

The platform combines machine learning predictions with an interactive analytics dashboard to provide actionable business insights.

---

## Features

* AI-powered revenue forecasting
* Marketing channel performance analysis
* ROAS prediction and optimization insights
* CSV-based ecommerce data ingestion
* Automated feature generation pipeline
* Machine learning prediction engine
* Interactive business intelligence dashboard
* Google Authentication with Firebase
* Revenue trend monitoring
* Risk and opportunity detection
* Channel intelligence scoring
* What-if budget simulation
* Forecast confidence analysis
* Revenue probability estimation

---

## Tech Stack

### Frontend

* React
* Firebase Authentication
* Interactive Analytics Dashboard

### Backend

* Python 3.11
* Pandas
* Scikit-Learn
* Joblib

### Machine Learning

* Random Forest Regression
* Automated Feature Engineering
* Revenue Prediction Pipeline

---

## Repository Structure

```text
LuminaAI/
├── data/
├── pickle/
│   └── model.pkl
├── src/
├── run.sh
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Python Version

Python 3.11 recommended

---

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Train Model

```bash
python src/train_model.py
```

---

## Run Predictions

```bash
bash run.sh ./data ./pickle/model.pkl ./output/predictions.csv
```

---

## Output

Predictions are generated at:

```text
output/predictions.csv
```

---

## Use Cases

* Ecommerce revenue forecasting
* Marketing budget optimization
* ROAS monitoring
* Campaign performance analysis
* Business intelligence reporting
* Risk detection and forecasting

---

## Future Enhancements

* Advanced forecasting models
* Real-time analytics API
* Automated anomaly detection
* Multi-model ensemble forecasting
* AI-generated business recommendations

---

## Author

Riddhi Patel

