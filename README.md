# Telco Churn Prediction Project

## Overview

This project focuses on predicting customer churn for a telecommunications company using machine learning techniques. The business objective is to proactively identify customers who are likely to churn so that retention strategies can be implemented, ultimately reducing revenue loss and increasing customer lifetime value.  

From a business perspective, **reducing churn is critical**, as acquiring a new customer can cost 5-7 times more than retaining an existing one. Predicting churn allows marketing and customer success teams to target at-risk customers with personalized offers and interventions.

---

## Business Problem

- **Problem Statement:** Identify customers at risk of leaving the company.  
- **Objective:** Maximize retention by targeting interventions effectively.  
- **Metric Focus:** **Recall** — because it is more important to identify as many churners as possible, even at the cost of some false positives. Missing a potential churner could result in lost revenue.

---

## Dataset

The dataset used in this project is [Telco Customer Churn Dataset](telco_churn.csv), which includes features related to customer demographics, account information, and service usage.  

**Key features include:**  

- `gender`, `SeniorCitizen`, `Partner`, `Dependents`  
- `tenure`, `Contract`, `PaymentMethod`  
- `MonthlyCharges`, `TotalCharges`  
- Service features: `PhoneService`, `InternetService`, `OnlineSecurity`, `TechSupport`, `StreamingTV`, `StreamingMovies`

---

## Modeling Approach

A structured machine learning pipeline was used to preprocess the data and evaluate multiple algorithms. The workflow included:

1. **Data Preprocessing**  
   - Handling categorical variables with **One-Hot Encoding**  
   - Scaling numerical features with **StandardScaler**  
   - Handling missing values and data inconsistencies

2. **Modeling**  
   - Baseline models tested for benchmarking  
   - Hyperparameter optimization to improve recall  

3. **Evaluation Metrics**  
   - **Accuracy**: measures overall correctness  
   - **Precision**: fraction of predicted churners that actually churned  
   - **Recall**: fraction of actual churners correctly identified (**primary metric**)  
   - **F1-score**: harmonic mean of precision and recall  

| Metric    | Baseline | Optimized |
|-----------|----------|-----------|
| Accuracy  | 0.794890 | 0.737402  |
| Precision | 0.636656 | 0.503367  |
| Recall    | 0.529412 | 0.799465  |
| F1-score  | 0.578102 | 0.617769  |

> The optimized model significantly increased recall, which aligns with the business goal of capturing as many churners as possible.

---

## Production Deployment

The final model is deployed on **Streamlit** for interactive exploration and real-time predictions:  

https://telcochurn-55b3vcch8e4frauuszw6tf.streamlit.app/  

---

## Next Steps

1. **Model Monitoring:** Track performance metrics as new data is added to ensure the model continues to perform well.  
2. **Retraining Strategy:** If recall or other metrics degrade, retraining will be necessary to maintain predictive power.  
3. **Feature Expansion:** Incorporate new behavioral or usage data to further improve model accuracy and recall.  
4. **Business Integration:** Collaborate with marketing and customer success teams to operationalize retention strategies based on model predictions.

---

## Conclusion

This project demonstrates a **data-driven approach to customer retention**, balancing technical rigor with business impact. By prioritizing recall, the model ensures that the company can proactively engage at-risk customers, ultimately safeguarding revenue and enhancing customer loyalty.  

---
