# Loan Approval Prediction

An end-to-end machine learning project that predicts whether a loan application will be **Approved** or **Rejected**, based on applicant details such as income, CIBIL score, assets, and employment status. The trained model is deployed as an interactive web app using **Streamlit**.

## Live Demo

_Add your deployed Streamlit app link here once hosted on Streamlit Community Cloud._

## Overview

This project covers the complete machine learning workflow:

- Exploratory Data Analysis (EDA)
- Data cleaning (handling invalid/negative values, whitespace in columns)
- Categorical encoding
- Correlation analysis
- Model training using Random Forest
- Hyperparameter tuning with GridSearchCV
- Model evaluation (accuracy, confusion matrix, classification report, feature importance)
- Overfitting analysis (train vs. test accuracy comparison)
- Deployment as a Streamlit web app with input validation

## Dataset

The dataset used is the **Loan Approval Prediction Dataset** from Kaggle, containing 4,269 loan applications with the following features:

| Feature | Description |
|---|---|
| `no_of_dependents` | Number of people financially dependent on the applicant |
| `education` | Graduate / Not Graduate |
| `self_employed` | Whether the applicant is self-employed |
| `income_annum` | Annual income of the applicant |
| `loan_amount` | Requested loan amount |
| `loan_term` | Loan repayment term (in years) |
| `cibil_score` | Applicant's CIBIL credit score (300–900) |
| `residential_assets_value` | Value of residential property owned |
| `commercial_assets_value` | Value of commercial property owned |
| `luxury_assets_value` | Value of luxury assets owned |
| `bank_asset_value` | Value of bank/savings assets |
| `loan_status` | Target variable — Approved / Rejected |

## Data Cleaning

- Stripped leading/trailing whitespace from column names and categorical values.
- Found 28 rows (0.65%) with an invalid negative value (`-100000`) in `residential_assets_value`; replaced with `0`.
- Verified no missing values and no duplicate rows.
- Encoded categorical columns (`education`, `self_employed`, `loan_status`) to numeric (0/1).

## Exploratory Data Analysis

A correlation heatmap was used to study relationships between features:

- `cibil_score` showed a strong correlation (**0.77**) with `loan_status` — the single strongest predictor.
- Income and asset-related columns were highly correlated with each other (multicollinearity), which is not an issue for tree-based models like Random Forest.
- `education`, `self_employed`, and `no_of_dependents` showed near-zero linear correlation with the target individually.

## Model Training

- **Algorithm:** Random Forest Classifier
- **Train/Test Split:** 80/20, stratified on the target variable
- **Hyperparameter Tuning:** GridSearchCV (5-fold cross-validation) over `n_estimators`, `max_depth`, `max_features`, and `min_samples_split`

**Best Parameters:**
```
{'max_depth': 15, 'max_features': 8, 'min_samples_split': 2, 'n_estimators': 200}
```

## Results

| Metric | Score |
|---|---|
| Test Accuracy | 98.0% |
| Precision (Approved) | 0.98 |
| Recall (Approved) | 0.99 |
| Precision (Rejected) | 0.98 |
| Recall (Rejected) | 0.97 |

**Feature Importance:** `cibil_score` alone accounts for ~83% of the model's decision-making importance, confirming it as the dominant factor in loan approval — consistent with real-world lending practices.

**Overfitting Check:** Training accuracy was 100% vs. 98% test accuracy — a small, acceptable gap indicating mild overfitting, not a generalization failure.

## Tech Stack

- **Python**
- **Pandas / NumPy** – data manipulation
- **Scikit-learn** – model training, tuning, evaluation
- **Seaborn / Matplotlib** – EDA visualizations
- **Streamlit** – web app deployment
- **Pickle** – model serialization

## Project Structure

```
├── loan_approval_dataset.csv     # Dataset
├── eda.ipynb                     # EDA, cleaning, model training & tuning
├── app.py                        # Streamlit web app
├── random.pkl                    # Saved trained model
├── requirements.txt               # Project dependencies
└── README.md
```

## How to Run Locally

1. Clone the repository:
```bash
git clone <your-repo-url>
cd <repo-folder>
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the Streamlit app:
```bash
streamlit run app.py
```

## App Features

- Interactive input form covering all 11 model features.
- Input fields constrained to the training dataset's value ranges to keep predictions reliable.
- A disclaimer explaining this is a demo model and predictions outside the trained data range may be unreliable.
- Instant Approved / Rejected prediction on button click.

## Limitations & Future Improvements

- The model has only been trained on the value ranges present in this dataset; inputs far outside those ranges (e.g., income or CIBIL score at the extreme edges) may produce unreliable predictions.
- Potential future additions: engineered features like `debt_to_income_ratio` and `total_assets_value`, comparison against XGBoost/Gradient Boosting, and displaying prediction confidence (`predict_proba`) alongside the result.

## Author

Aditya
BCA (AI & Data Science) student, building a portfolio in Machine Learning with future goals in Generative AI and Agentic AI.
