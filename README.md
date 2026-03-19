# Customer-Churn-Analysis-Prediction-Dashboard
#Project Overview
This project focuses on analyzing customer churn and predicting high-risk customers using Machine Learning and Power BI.
The goal is to identify why customers leave and provide actionable insights to reduce churn.

#Tech Stack
Python (Pandas, NumPy, Scikit-learn)
Machine Learning (Random Forest)
Power BI (Dashboard & Visualization)
SQL (Data handling - optional)

#Project Structure
churn-analysis-project/
│
├── data/
│   ├── raw_data.csv
│   └── churn_predictions.csv
│
├── src/
│   ├── data_preprocessing.py
│   ├── model_training.py
│   ├── prediction.py
│
├── dashboard/
│   └── powerbi_dashboard.pbix
│
├── main.py
├── requirements.txt
└── README.md

#Machine Learning Model
Model Used: Random Forest Classifier
Accuracy: ~80%

#Output:
Churn Prediction (0/1)
Churn Probability (risk score)

🔹 Insights
Month-to-month customers have higher churn
Higher monthly charges increase churn risk
Customers with low tenure are more likely to churn
High-risk customers identified using ML predictions

#How to Run
Install dependencies
pip install -r requirements.txt

Run the project
python main.py

Open Power BI dashboard
dashboard/powerbi_dashboard.pbix

#Dashboard Preview

<img width="1284" height="722" alt="image" src="https://github.com/user-attachments/assets/553bc139-16ad-4847-a9e0-d316b6044503" />
