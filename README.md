# 🏦 Bank Customer Churn Prediction using PySpark

This project predicts bank customer churn using scalable machine learning models built with **PySpark MLlib**. The goal is to identify customers who are likely to leave the bank and provide insights that can help improve retention strategies.

---

## 📌 Project Overview

Customer churn is a major challenge in the banking sector. Retaining customers is more cost-effective than acquiring new ones. This project uses **Big Data analytics and distributed machine learning** to predict churn using real-world customer data.

Built as part of a **Big Data Analytics Lab mini project**.

---

## 📊 Dataset

- **Source:** Kaggle – Bank Customer Churn Dataset  
- **Records:** 10,000 customers  
- **Features:** Demographic and account data

### Key Attributes:
- Credit Score
- Geography
- Gender
- Age
- Tenure
- Balance
- Number of Products
- Active Member Status
- Estimated Salary
- Target: `Exited` (0 = Retained, 1 = Churned)

---

## 🛠 Tech Stack

- **Language:** Python  
- **Framework:** PySpark (Apache Spark MLlib)  
- **Platform:** Google Colab  
- **Libraries:**
  - pyspark.sql
  - pyspark.ml (classification, feature engineering, evaluation)

---

## ⚙️ Methodology

### 1. Data Preprocessing
- Removed irrelevant columns (CustomerId, Surname, RowNumber)
- Handled categorical features using:
  - StringIndexer
  - OneHotEncoder
- Combined features using VectorAssembler
- Train-test split: 80:20

---

### 2. Models Implemented

- Logistic Regression (baseline)
- Random Forest Classifier
- Gradient Boosted Trees (GBT)

All models built using **PySpark ML Pipelines**.

---

## 📈 Results

| Model | AUC | Accuracy |
|------|-----|----------|
| Logistic Regression | 0.76 | 81.1% |
| Random Forest | 0.83 | 85.1% |
| Gradient Boosted Trees | **0.85** | **85.2%** |

✅ **Best Model:** Gradient Boosted Trees

---

## 🔍 Key Insights

- Age is the strongest churn predictor
- Customers with fewer products are more likely to churn
- Inactive members have higher churn probability
- Tree-based models outperform linear models for churn prediction

These insights can help banks design targeted retention strategies.

---

## 🚀 How to Run

1. Install PySpark:
pip install pyspark

2. Run the notebook using:
- Google Colab (recommended)  
- Jupyter Notebook  

3. Upload the dataset (CSV) and run all cells sequentially.

---

## 📚 Learnings

- Built end-to-end ML pipeline using PySpark  
- Learned feature engineering with Spark ML  
- Compared multiple classification models  
- Understood Big Data processing using distributed computing  
- Gained practical experience with churn prediction  

---

## 🔮 Future Improvements

- Hyperparameter tuning  
- Cross-validation  
- Feature selection optimization  
- Model deployment using Streamlit  
- Real-time churn prediction pipeline  

---

## 👩‍💻 Author

Meghana  

---

## ⭐ Support

If you found this project helpful, consider giving it a star ⭐
