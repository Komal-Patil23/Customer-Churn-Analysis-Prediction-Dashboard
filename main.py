from src.data_preprocessing import load_data, preprocess_data
from src.model_training import train_model
from src.prediction import make_predictions

df = load_data("data/raw_data.csv")

df = preprocess_data(df)

model, X = train_model(df)

make_predictions(model, X, df)