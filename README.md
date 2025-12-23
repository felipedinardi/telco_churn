# Telco Customer Churn Prediction

## Overview

This project aims to **predict customer churn** for a telecommunications company using machine learning. The business goal is to **proactively identify customers at risk of leaving**, allowing retention strategies to be applied and minimizing revenue loss.  

**Business Impact:** Retaining existing customers is much more cost-effective than acquiring new ones. By predicting churn, the company can target high-risk customers with personalized offers and support, improving **customer lifetime value** and loyalty.

---

## Business Problem

- **Objective:** Identify customers likely to churn.  
- **Primary Metric:** **Recall**, to ensure that as many churners as possible are correctly identified. Missing a potential churner could result in revenue loss.  
- **Secondary Metrics:** Accuracy, Precision, F1-score — tracked for model benchmarking.  

---

## Dataset

The dataset includes **demographic, account, and service-related features** of customers:

- Demographics: `gender`, `SeniorCitizen`, `Partner`, `Dependents`  
- Account Info: `tenure`, `Contract`, `PaymentMethod`, `PaperlessBilling`  
- Services: `PhoneService`, `MultipleLines`, `InternetService`, `OnlineSecurity`, `TechSupport`, `DeviceProtection`, `StreamingTV`, `StreamingMovies`  
- Charges: `MonthlyCharges`, `TotalCharges`  

Data cleaning included:
- Converting **Yes/No** to **0/1**  
- Replacing `'No internet service'` / `'No phone service'` with `'No'`  
- Filling missing `TotalCharges` with `tenure * MonthlyCharges`  
- One-Hot Encoding for categorical variables  
- Scaling numeric features using `StandardScaler`

---

## Modeling Approach

1. **Model Comparison**  
   - Tested multiple models using cross-validation with **StratifiedKFold**:  
     - Logistic Regression  
     - Decision Tree  
     - Random Forest  
     - XGBoost  
   - Evaluated using **recall**, prioritizing business need.  
   
2. **Baseline Model**  
   - Logistic Regression with default hyperparameters.  

3. **Hyperparameter Tuning**  
   - Grid search applied to Logistic Regression for optimal:  
     - `C`, `solver`, `penalty`, `class_weight`  
   - Focused on maximizing **recall**.  

4. **Evaluation Metrics**

| Metric    | Baseline | Optimized |
|-----------|----------|-----------|
| Accuracy  | 0.794890 | 0.737402  |
| Precision | 0.636656 | 0.503367  |
| Recall    | 0.529412 | 0.799465  |
| F1-score  | 0.578102 | 0.617769  |

> The optimized model significantly improved recall, achieving the business goal of **catching more churners**.  

---

## Deployment

The final model is deployed for interactive use via **Streamlit**:  

[Open the App](https://telcochurn-55b3vcch8e4frauuszw6tf.streamlit.app/)  

**Saved artifacts:**  
- `churn_model.pkl` → Trained optimized model  
- `model_columns.pkl` → Columns used in training

---

## Next Steps

1. **Model Monitoring:** Track recall and other metrics as new customer data becomes available.  
2. **Retraining:** If performance drops, retraining with new data will be performed.  
3. **Feature Expansion:** Include new behavioral or service usage features to further enhance predictions.  
4. **Business Integration:** Collaborate with marketing and customer success teams to leverage predictions in retention campaigns.  

---

## Conclusion

This project demonstrates a **data-driven approach to reducing churn**, combining **robust technical methodology** with **business impact**. By prioritizing recall, the model ensures **maximum identification of at-risk customers**, helping the company protect revenue and enhance customer loyalty.

---
