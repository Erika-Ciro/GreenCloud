# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.metrics import r2_score, mean_squared_error, accuracy_score, classification_report
from sklearn.model_selection import train_test_split

# ------------------- 1. Regression Models -------------------

def regression_analysis(df):
    """
    Explores regression models to predict 'Consolidated Grid Carbon Intensity (gCO2eq / kWh)'.
    """
    # Prepare data for regression
    X_reg = df[['Google CFE']]
    y_reg = df['Consolidated Grid Carbon Intensity (gCO2eq / kWh)']
    
    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X_reg, y_reg, test_size=0.2, random_state=42)
    
    # Linear Regression
    lin_reg = LinearRegression()
    lin_reg.fit(X_train, y_train)
    y_pred = lin_reg.predict(X_test)
    print("Linear Regression Results:")
    print(f"R² Score: {r2_score(y_test, y_pred):.2f}")
    print(f"Mean Squared Error: {mean_squared_error(y_test, y_pred):.2f}\n")
    
    # Random Forest Regressor
    rf_reg = RandomForestRegressor(random_state=42)
    rf_reg.fit(X_train, y_train)
    y_pred_rf = rf_reg.predict(X_test)
    print("Random Forest Regressor Results:")
    print(f"R² Score: {r2_score(y_test, y_pred_rf):.2f}")
    print(f"Mean Squared Error: {mean_squared_error(y_test, y_pred_rf):.2f}\n")

# ------------------- 2. Classification Models -------------------

def classification_analysis(df):
    """
    Explores classification models to categorize locations based on 'Google CFE'.
    """
    # Feature Engineering: Add High/Low CFE classification
    df['Google CFE High/Low'] = (df['Google CFE'] > 0.5).astype(int)
    
    # Prepare data for classification
    X_clf = df[['Consolidated Grid Carbon Intensity (gCO2eq / kWh)']]
    y_clf = df['Google CFE High/Low']
    X_train, X_test, y_train, y_test = train_test_split(X_clf, y_clf, test_size=0.2, random_state=42)
    
    # Logistic Regression
    log_reg = LogisticRegression()
    log_reg.fit(X_train, y_train)
    y_pred = log_reg.predict(X_test)
    print("Logistic Regression Results:")
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
    print(f"Classification Report:\n{classification_report(y_test, y_pred)}\n")
    
    # Random Forest Classifier
    rf_clf = RandomForestClassifier(random_state=42)
    rf_clf.fit(X_train, y_train)
    y_pred_rf = rf_clf.predict(X_test)
    print("Random Forest Classifier Results:")
    print(f"Accuracy: {accuracy_score(y_test, y_pred_rf):.2f}")
    print(f"Classification Report:\n{classification_report(y_test, y_pred_rf)}\n")

# ------------------- 3. Main Function -------------------

if __name__ == "__main__":
    # Example usage
    print("Loading prepared data...")
    # Replace this with the actual prepared dataset path
    df = pd.read_csv("data/processed/google_cfe_2019_2023.csv")
    
    print("\nRunning Regression Analysis...")
    regression_analysis(df)
    
    print("\nRunning Classification Analysis...")
    classification_analysis(df)
