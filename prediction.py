def make_predictions(model, X, df):
    df['churn_prediction'] = model.predict(X)
    df['churn_probability'] = model.predict_proba(X)[:,1]

    df.to_csv("data/churn_predictions.csv", index=False)

    print("Predictions saved!")