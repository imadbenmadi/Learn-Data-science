# **Medical Insurance Charges Analysis & Prediction**

## **📌 Project Overview**

This project aims to **analyze and predict medical insurance charges** based on various factors such as **age, BMI, smoking habits, and region**. Using **data analytics and machine learning**, I explore how these factors influence insurance costs and build predictive models to estimate charges.

## **📊 Dataset Overview**

The dataset is a filtered version of the **Medical Insurance Price Prediction** dataset from Kaggle. It contains:

-   **Demographics**: Age, gender, region
-   **Health Factors**: BMI, smoker status
-   **Family Details**: Number of children
-   **Financial Factor**: Insurance charges (USD)

## **🎯 Objectives**

✔️ Load and clean the dataset  
✔️ Perform **exploratory data analysis (EDA)** to find patterns & insights  
✔️ Develop **Single & Multiple Linear Regression models** for predictions  
✔️ Improve model performance using **Ridge Regression**  
✔️ Visualize key findings with **Seaborn & Matplotlib**  
✔️ (Optional) Build an **interactive Tableau dashboard**

## **📈 Key Insights & Findings**

🔹 Smokers pay significantly higher insurance charges than non-smokers  
🔹 BMI and age have a strong impact on insurance costs  
🔹 The **Southeast region** tends to have the highest average charges

## **🔍 Machine Learning Models Used**

-   **Linear Regression** (Single & Multi-variable)
-   **Polynomial Regression** (To capture non-linear relationships)
-   **Ridge Regression** (To prevent overfitting & improve predictions)


## 📌 Key Steps:

✅ Exploratory Data Analysis (EDA) – Cleaning, transformations, and understanding trends 📊

✅ Feature Engineering – Handling categorical and numerical features

✅ Model Training & Validation – From basic regression to polynomial regression with cross-validation

✅ Hyperparameter Tuning – Finding the best degree and regularization (Ridge Regression) 🔥

✅ Visualizing Performance – Score plots, distribution plots, and comparisons of different models

🔍 After trying random splits, cross-validation, and polynomial transformations, I optimized the final model to achieve the best balance between performance and generalization.

This project was a great hands-on experience in Data Science & Machine Learning, and I’m excited for more! 🚀
Final Best Choice: k=6, Degree=2
R2: 84.0%
MSE: 23700278.168564092
## Explotary Data Analysis 
![alt text](<reports/figures/EDA/box plot for charges with respect to smoker.png>)
This box plot compares insurance charges between smokers and non-smokers. Key insights:

1. **Smokers pay significantly higher charges**: The median insurance cost for smokers is much higher than for non-smokers.
2. **Wider spread among smokers**: The range (interquartile range and whiskers) for smokers is much larger, indicating high variability in insurance costs.
3. **More outliers in non-smokers**: While non-smokers generally have lower charges, there are several outliers with higher costs.
4. **Clear distinction**: Smoking status is a strong factor influencing insurance charges, likely due to increased health risks associated with smoking.

This suggests that smoking has a major financial impact on insurance costs.
-----
![alt text](<reports/figures/EDA/correlation Heat map.png>)
This heatmap represents the correlation matrix of variables related to insurance charges. Key insights:
1. **Age vs. Charges (0.30)**: Moderate positive correlation, indicating that older individuals tend to have higher insurance charges.
2. **BMI vs. Charges (0.20)**: Weak positive correlation, suggesting that higher BMI may slightly contribute to higher insurance costs.
3. **No. of Children vs. Charges (0.07)**: Very weak correlation, implying that the number of children has little impact on insurance charges.
4. **Age vs. BMI (0.11)** and **Age vs. No. of Children (0.04)**: Almost no correlation, showing that these factors are independent.
Overall, age has the strongest impact on charges, while the number of children is almost irrelevant. 
----
## Code snaps :
### use cross validation with polynomial regression
The code uses **5-fold cross-validation** to determine the best polynomial degree for regression. It iterates through degrees **1 to 10**, selecting the one with the **highest mean R² score** while avoiding overfitting (negative R²). The final model is trained using this optimal degree, and its performance is evaluated with **R², MSE, and distribution plots** of actual vs. predicted values.
![alt text](<images/using cross validation with polynomial regression.png>)
-----
### final model traing code :
![alt text](<images/final model traing code.png>)
### final score and mse:
![alt text](<reports/figures/Best R² Score for Different K-Folds.png>)
-----
### distribution plot of the final model : 
![alt text](<reports/figures/Hyper-params tuning using Piplines (grid search + ridge regression + cv).png>)
---
## **📌 Project Demo & GitHub Link**

<!-- 🔗 [Tableau Dashboard (if applicable)](your_tableau_link_here)   -->

🔗 [GitHub Repository](https://github.com/imadbenmadi/Medical-Insurance-Price-Prediction)

🔗 [Kaggle ](https://www.kaggle.com/code/imedbenmadi/notebook628d4598db)

----

🔗 [Data Set started Csv file](https://github.com/imadbenmadi/Medical-Insurance-Price-Prediction/blob/main/data/Medical_insurance.csv)

🔗 [Data Set cleaned Csv file](https://github.com/imadbenmadi/Medical-Insurance-Price-Prediction/blob/main/data/cleaned_data.csv)

🔗 [Data Set Link](https://www.kaggle.com/datasets/harishkumardatalab/medical-insurance-price-prediction?resource=download)

💡 If you liked this project, **drop a star ⭐ on GitHub!**
