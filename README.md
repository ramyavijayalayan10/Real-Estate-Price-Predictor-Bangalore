# 🏠 Real Estate Price Predictor - Bangalore

A complete Machine Learning web application to predict real estate prices in Bangalore based on location, square footage, and number of bedrooms/bathrooms.  
Built using Google Colab, trained with Scikit-Learn, served with Flask, and deployed publicly via Render.  

![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey)
![Made with Flask](https://img.shields.io/badge/Backend-Flask-blue)
![Built in Google Colab](https://img.shields.io/badge/Notebook-Google%20Colab-yellow)
![Deployed on Render](https://img.shields.io/badge/Hosted%20on-Render-green)

---

## 🎬 Demo

📺 [Watch a demo video](https://drive.google.com/your-demo-link-here)  
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

All model building steps are documented in a single Google Colab notebook:

- ✅ Data Wrangling
- 📈 Exploratory Data Analysis (EDA)
- ✂️ Outlier Removal
- 🧪 Feature Engineering
- 🧠 Model Selection & Training (Linear Regression)
- 📦 Exporting model as `.pkl` for Flask usage

📁 See notebook: [`model-training/Bangalore_Price_Prediction_Colab.ipynb`](model-training/Bangalore_Price_Prediction_Colab.ipynb)

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
bangalore-price-predictor/
├── model-training/       # Colab notebook with full ML pipeline
│   └── Bangalore_Price_Prediction_Colab.ipynb
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

