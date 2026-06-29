# Student-Performance-Project
End-to-end Student Performance Analytics project using Python, SQL, Power BI, and Machine Learning.
# 🎓 Student Performance Analytics

## 📌 Project Overview

This project analyzes student academic performance using Python, SQL, Power BI, and Machine Learning. The objective is to identify the factors that influence students' exam scores, generate business insights through exploratory data analysis, build an interactive dashboard, and develop predictive models for estimating exam performance.

## 🎯 Project Objectives

- Clean and preprocess the dataset
- Perform Exploratory Data Analysis (EDA)
- Answer business questions using Python and SQL
- Build an interactive Power BI dashboard
- Train and compare machine learning models
- Predict student exam scores

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- SQL (MySQL)
- Power BI
- Scikit-learn

## 📂 Project Workflow

Business Understanding

↓

Data Cleaning

↓

Exploratory Data Analysis

↓

SQL Business Analysis

↓

Power BI Dashboard

↓

Machine Learning

↓

Business Recommendations

## ❓ Business Questions Explored

This project investigates the following business questions:

1. Does studying more hours improve exam performance?
2. Does higher attendance lead to better exam scores?
3. Do tutoring sessions significantly improve student performance?
4. Does parental involvement affect academic success?
5. Does sleep duration influence exam scores?
6. Do previous academic scores predict future performance?
7. Does teacher quality impact exam results?
8. Does motivation level affect student performance?
9. Does family income influence exam scores?
10. Does internet access improve academic performance?
11. Do learning disabilities significantly affect exam scores?
12. Is there any difference in exam performance based on gender?

## 📊 Key Findings

- Attendance showed the strongest positive relationship with exam performance (Correlation ≈ 0.58).
- Study hours had a moderate positive relationship with exam scores (Correlation ≈ 0.45).
- Previous academic scores showed only a weak positive relationship with current exam scores.
- Tutoring sessions resulted in only a small improvement in average exam scores.
- Teacher quality, motivation level, family income, internet access, and parental involvement showed only minor differences in average exam scores.
- Gender showed almost no difference in academic performance.
- Student performance appears to be influenced by multiple factors rather than one single factor.

## 🤖 Machine Learning

Two regression models were trained and evaluated:

| Model | MAE | RMSE | R² Score |

| Linear Regression | 0.45 | 1.80 | 0.77 |
| Decision Tree Regressor | 1.98 | 3.74 | 0.01 |

### Conclusion

Linear Regression significantly outperformed the Decision Tree model and was selected as the final predictive model. The model explained approximately **77%** of the variation in student exam scores while maintaining a very low prediction error.

