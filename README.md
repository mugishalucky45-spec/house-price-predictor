# Rwanda House Price Predictor

## Project Purpose

This project develops a machine learning model that predicts house prices in Rwanda using multiple linear regression. The prediction is based on house characteristics such as area, bedrooms, bathrooms, house age, distance to the city centre, parking spaces, and neighbourhood.

The trained model is also provided through an interactive Streamlit web application.

## Dataset

The dataset contains house information and prices in million Rwandan Francs (RWF).

### Features

- Area_m2
- Bedrooms
- Bathrooms
- House_Age_Years
- Distance_to_City_km
- Parking_Spaces
- Neighborhood

### Target

- House_Price_Million_RWF

`House_ID` was excluded from the model because it is only an identifier.

## Data Preparation

The dataset was inspected and cleaned before modelling. The categorical `Neighborhood` variable was encoded using one-hot encoding, with one category dropped to avoid the dummy-variable trap.

The data was divided into:

- 80% training data
- 20% testing data

The split used `random_state=42`.

## Model

A Multiple Linear Regression model was developed using scikit-learn.

The preprocessing and regression model were combined into a pipeline so that the saved model can receive the original input features directly.

The trained pipeline was saved as:

`house_price_model.sav`

## Model Performance

The model was evaluated using R², adjusted R², MAE, and RMSE on both the training and testing datasets.

### R²

Add the R² values from the notebook here.

### RMSE

Add the RMSE values from the notebook here.

## Streamlit Application

The Streamlit application allows a user to enter:

1. Area
2. Bedrooms
3. Bathrooms
4. House age
5. Distance to city
6. Parking spaces
7. Neighborhood

The application then predicts the estimated house price in million RWF.

## Files in This Repository

- `app.py` — Streamlit application
- `house_price_model.sav` — trained machine learning model
- `house_price_prediction_cleaned.csv` — cleaned dataset
- `house prediction.ipynb` — Jupyter Notebook containing the analysis and modelling
- `requirements.txt` — Python dependencies
- `README.md` — project documentation

## How to Run Locally

Install the required packages:

```bash
pip install -r requirements.txt
