
import numpy as np
import pandas as pd

data=pd.read_csv("StudentPerformanceFactors.csv")
df=pd.DataFrame(data)

# First 10 rows
print(df.head(10))

# replacing the categorical values with the mode as we cannot find the mean.
df["Teacher_Quality"]=df["Teacher_Quality"].fillna(df["Teacher_Quality"].mode()[0])
df["Parental_Education_Level"]=df["Parental_Education_Level"].fillna(df["Parental_Education_Level"].mode()[0])
df["Distance_from_Home"]=df["Distance_from_Home"].fillna(df["Distance_from_Home"].mode()[0])

# features and target
y=df["Exam_Score"]
X=df.drop("Exam_Score",axis=1)

# one-hot encoding
X = pd.get_dummies(X,drop_first=True)
'''This avoids creating unnecessary duplicate information for the model.'''
print(X.head())
print(X.shape)

# train test split
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

print("\n Training features : ",X_train.shape)
print("\n Testing features : ",X_test.shape)
print("\nTraining Target :", y_train.shape)
print("\nTesting Target  :", y_test.shape)

# =====================================
# Linear Regression Model
# =====================================

from sklearn.linear_model import LinearRegression
lr_model=LinearRegression()
lr_model.fit(X_train,y_train)
lr_pred = lr_model.predict(X_test)

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

lr_mae=mean_absolute_error(y_test,lr_pred)
lr_mse=mean_squared_error(y_test,lr_pred)
lr_rmse=np.sqrt(lr_mse)
lr_r2=r2_score(y_test,lr_pred)

print("\nLinear regression results :- ")
print("MAE :", lr_mae)
print("MSE :", lr_mse)
print("RMSE:", lr_rmse)
print("R² Score:", lr_r2)
'''The Linear Regression model successfully predicts student exam scores with good accuracy.
The low prediction error and R² score of 0.77 suggest that academic and personal factors 
such as attendance, study hours, previous scores, and motivation collectively
provide a strong basis for predicting student performance.'''

# =====================================
# Decision Tree Regression Model
# =====================================

from sklearn.tree import DecisionTreeRegressor
dt_model=DecisionTreeRegressor(random_state=42)# as exam score is continuous 
#                                               so we will use the regression version
dt_model.fit(X_train,y_train)

dt_pred=dt_model.predict(X_test)

dt_mae = mean_absolute_error(y_test,dt_pred)
dt_mse = mean_squared_error(y_test,dt_pred)
dt_rmse = np.sqrt(dt_mse)
dt_r2 = r2_score(y_test,dt_pred)

print("\nDecision tree results :- ")
print("MAE :", dt_mae)
print("MSE :", dt_mse)
print("RMSE:", dt_rmse)
print("R² Score:", dt_r2)

# Comparision
print("\n Comparision bw both models:\n")
comparision=pd.DataFrame({
    "Model":["Linear Regression","Decision Tree"],
    "MAE":[lr_mae,dt_mae],
    "MSE":[lr_mse,dt_mse],
    "RMSE":[lr_rmse,dt_rmse],
    "R2 score":[lr_r2,dt_r2]
})
print(comparision.round(2)) # round off to 2 digits

print("\nBusiness Conclusion:")
print( "Linear Regression performed very well than Decision Tree "
       "and is recommended for predicting student exam scores.")