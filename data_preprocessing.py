import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def preprocess_data(df):
    # Drop customer ID (not useful for ML)
    df.drop("customerID", axis=1, inplace=True)

    # Convert TotalCharges to numeric
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

    # Handle missing values
    df.fillna(df.mean(numeric_only=True), inplace=True)

    # Convert target column (Yes/No → 1/0)
    df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

    # Convert categorical columns
    df = pd.get_dummies(df, drop_first=True)

    return df