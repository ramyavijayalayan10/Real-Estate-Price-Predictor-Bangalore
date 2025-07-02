# 🏠 Real Estate Price Predictor - Bangalore

A complete Machine Learning web application to predict real estate prices in Bangalore based on location, square footage, and number of bedrooms/bathrooms.  
Built using Google Colab, trained with Scikit-Learn, served with Flask, and deployed publicly via Render.  

![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey)
![Made with Flask](https://img.shields.io/badge/Backend-Flask-blue)
![Built in Google Colab](https://img.shields.io/badge/Notebook-Google%20Colab-yellow)
![Deployed on Render](https://img.shields.io/badge/Hosted%20on-Render-green)

---

## 🎬 Demo

📺 [Watch a demo video](https://drive.google.com/file/d/1hx4aatWpMAmCRBfmODvfTPj2Z17UD0Qm/view?usp=sharing)  
🌐 [Try the live app](https://your-app-url.onrender.com)

---

## 🧠 About the Project

This web app allows users to estimate housing prices in Bangalore by inputting:

- Total square footage
- Number of BHKs
- Number of bathrooms
- Neighborhood location

The model was trained on real housing data, cleaned and engineered inside a Google Colab notebook. It uses a regression algorithm optimized through outlier removal, feature selection, and cross-validation. Predictions are served in real time via a Flask API, and the frontend uses plain HTML, CSS, and JavaScript.

---

## 📊 Model Training & EDA

This notebook was originally developed in **Google Colab** and later adapted for local execution. 
It contains the complete machine learning pipeline:

- ✅ Data Wrangling
- 📈 Exploratory Data Analysis (EDA)
- ✂️ Outlier Removal
- 🧪 Feature Engineering
- 🧠 Model Selection & Training (Linear Regression)
- 📦 Exporting model as `.pkl` for Flask usage

📁 See notebook: [`model-training/Bangalore_Price_Prediction_Colab.ipynb`](model-training/Bangalore_Price_Prediction_Colab.ipynb)
Compatible with both Google Colab and VS Code. Dataset assumed to be stored locally in the `/data/` folder.

---

## ⚙️ Tech Stack

| Layer      | Technology Used              |
|------------|------------------------------|
| Data & ML  | Python, Pandas, NumPy, Matplotlib, Seaborn, Scikit-Learn |
| Training   | Google Colab (Jupyter-compatible notebook) |
| Backend    | Flask (API endpoint for predictions) |
| Frontend   | HTML, CSS, JavaScript |
| Hosting    | Render |
| Demo Video | Google Drive |

---

## 📁 Folder Structure

```bash
bangalore-real-estate-price-predictor/
├── model-training/       # Colab notebook with full ML pipeline
│   └── Real_Estate_Price_Prediction_Bangalore.ipynb
├── data/                 # Cleaned dataset 
│   └── cleaned_data.csv
├── model/                # Trained model file
│   └── price_model.pkl
├── api/                  # Flask API for prediction
│   └── app.py
├── client/               # Frontend files
│   ├── index.html
│   ├── app.css
│   └── app.js
├── demo/                 # Demo video 
│   └── app-demo.mp4
├── requirements.txt      # Python dependencies
├── LICENSE.md            # License terms (CC BY-NC-ND 4.0)
└── README.md             # Project overview and setup
```

## 📜 License

This project is licensed under the Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License.  
View full terms in [LICENSE.md](LICENSE.md) or [here](https://creativecommons.org/licenses/by-nc-nd/4.0/)

© Ramya Vijayalayan, 2025

---

## ✨ Credits

Created by Ramya Vijayalayan as a portfolio project  
Powered by data-driven insights and deployed via Render

