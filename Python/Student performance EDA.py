
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data=pd.read_csv("StudentPerformanceFactors.csv")
df=pd.DataFrame(data)

# First 10 rows
print(df.head(10))

# Shape
print("\n Shape of the dataset: ")
print(df.shape)

# Columns
print("\n columns are: ")
print(df.columns)

# Info
print("\n Info: ")
print(df.info())

# Missing values
print("\n Missing values: ")
print(df.isnull().sum())

# Duplicates
print("\n duplicates: ")
print(df.duplicated().sum())

# Statistical summary
print("\n Statistics summary")
print(df.describe())

# Unique Values
print("\nUnique Values Per Column:")
print(df.nunique())


# ==================================
# Data Cleaning
# ==================================

missing=df.isnull().sum()
missing=missing[missing>0]
print(missing)

# replacing the categorical values with the mode as we cannot find the mean.
df["Teacher_Quality"]=df["Teacher_Quality"].fillna(df["Teacher_Quality"].mode()[0])
df["Parental_Education_Level"]=df["Parental_Education_Level"].fillna(df["Parental_Education_Level"].mode()[0])
df["Distance_from_Home"]=df["Distance_from_Home"].fillna(df["Distance_from_Home"].mode()[0])

print(df.isnull().sum())

print(df[df["Exam_Score"]>101])

# ==================================
# Exploratory Data Analysis
# ==================================

'Exam score'
plt.figure(figsize=(10,6))
plt.hist(df["Exam_Score"], bins=15, edgecolor="black")
plt.title("Distribution of exam scores",color="purple",fontsize=15)
plt.xlabel("Exam score",color="olive",fontsize=10)
plt.ylabel("No. of students",color="olive",fontsize=10)
plt.savefig("exam score.png")
plt.tight_layout()
plt.show()

print("Average score: ",df["Exam_Score"].mean())
print("Highest score: ",df["Exam_Score"].max())
print("Lowest score: ",df["Exam_Score"].min())
print("Median exam score : ",df["Exam_Score"].median())

'''Exam Score Distribution
-> Most students scored between 60-70.
-> Highest concentration is around 65-69.
-> Very few students scored below 60.
-> Very few students scored above 75.
-> Distribution is approximately bell-shaped with a slight right skew.
-> Mean (67.23) and median (67) are very close, 
indicating the average score represents the dataset well.'''

# hours studied vs exam score

plt.scatter(df["Hours_Studied"],df["Exam_Score"],alpha=0.6,color="royalblue")
plt.title("Study hours vs exam score",color="purple",fontsize=15)
plt.xlabel("Hours studied",color="olive",fontsize=14)
plt.ylabel("Exam score",color='olive',fontsize=14)
plt.grid(alpha=0.3)
plt.savefig("exam_score_distribution.png")
plt.tight_layout()
plt.show()

study_corr = df["Hours_Studied"].corr(df["Exam_Score"])
print(f"\nCorrelation between Hours Studied and Exam Score: {study_corr:.2f}")

'''The analysis shows a moderate positive correlation (r = 0.45) between study hours and exam scores,
suggesting that students who study more tend to perform better. However, the relationship 
is not strong enough to conclude that study hours alone determine academic success. 
Other factors such as attendance, parental involvement, teacher quality, 
and motivation are also likely to influence exam performance. Additionally,
one unusually high score (101) should be investigated as a potential data anomaly.
'''

# Attendance vs exam score
plt.scatter(df["Attendance"],df["Exam_Score"],color='green',alpha=0.6)
plt.title("Atendance vs Exam score",color="purple",fontsize=15)
plt.xlabel("Attendance",color="olive",fontsize=15)
plt.ylabel("Exam score",color="olive",fontsize=15)
plt.grid(alpha=0.6)
plt.savefig("Attendance_vs_examscore .png")
plt.tight_layout()
plt.show()

Attendance_corr=df["Attendance"].corr(df["Exam_Score"])
print(f"\nCorrelation be attendance and exam score : {Attendance_corr:.2f}")

'''Attendance has a moderately strong positive relationship (r = 0.58) with exam scores,
indicating that students with higher attendance generally perform better.
However, the scatter plot also shows several students with relatively low attendance 
achieving high scores, suggesting that attendance is an important—but 
not the only—factor influencing academic performance.'''

# Do tutoring sessions improve students' exam performance?
tutoring_avg=df.groupby("Tutoring_Sessions")["Exam_Score"].mean()
print(tutoring_avg)

'''as scatter plot is better when we want to study the relationship between
individual data points.
A bar chart was chosen because the objective is to compare the average exam scores 
across different tutoring session groups. It provides a clearer comparison 
than a scatter plot for grouped data.'''
plt.bar(tutoring_avg.index, tutoring_avg.values,color="royalblue")
plt.title("Average Exam Score by Tutoring Sessions",color="purple",fontsize=15)
plt.xlabel("Tutoring Sessions",color="purple",fontsize=15)
plt.ylabel("Average Exam Score",color="purple",fontsize=15)
plt.grid(axis="y", alpha=0.3)
plt.savefig("tutoring_sessions.png")
plt.tight_layout()
plt.show()
'''Students attending more tutoring sessions tend to achieve slightly higher average
exam scores. However, the improvement is modest, suggesting that tutoring alone
is unlikely to be the primary factor determining academic performance.'''

# parental involvement
parent_avg = df.groupby("Parental_Involvement")["Exam_Score"].mean()
print(parent_avg)

plt.figure(figsize=(8,5))
plt.bar( parent_avg.index, parent_avg.values, color=["tomato","gold","seagreen"])
plt.title("Average Exam Score by Parental Involvement",color="purple",fontsize=15)
plt.xlabel("Parental Involvement",color="purple",fontsize=15)
plt.ylabel("Average Exam Score",color="purple",fontsize=15)
plt.grid(axis="y", alpha=0.3)
plt.savefig("parent involvement.png")
plt.tight_layout()
plt.show()

'''Students with higher parental involvement achieved slightly higher average exam scores
than students with medium or low parental involvement. However, the difference between 
the groups is relatively small (approximately 1.7 marks), suggesting that 
parental involvement alone is unlikely to be a major determinant of academic performance.'''

# Do sleep hours affect students' exam performance?
sleep_avg=df.groupby("Sleep_Hours")["Exam_Score"].mean()
print(sleep_avg)

plt.bar(sleep_avg.index,sleep_avg.values,color="mediumpurple")
plt.title("Average Exam Score by Sleep Hours",color="purple",fontsize=15)
plt.xlabel("Sleep Hours",color="purple",fontsize=15)
plt.ylabel("Average Exam Score",color="purple",fontsize=15)
plt.grid(axis="y", alpha=0.3)
plt.savefig("sleep hours.png")
plt.tight_layout()
plt.show()
'''The analysis indicates that sleep duration has little variation in average exam scores.
Students sleeping between 4 and 10 hours achieved very similar average scores, 
suggesting that sleep hours alone are not a significant predictor of academic performance
in this dataset.'''

# Do previous academic scores influence students' current exam scores?
# Previous Scores vs Exam Score

plt.figure(figsize=(8,5))
plt.scatter(df["Previous_Scores"],df["Exam_Score"],color="orange",alpha=0.6)
plt.title("Previous Scores vs Exam Score",color="purple",fontsize=15)
plt.xlabel("Previous Scores",color="purple",fontsize=15)
plt.ylabel("Exam Score",color="purple",fontsize=15)
plt.grid(alpha=0.3)
plt.savefig("previous scores.png")
plt.tight_layout()
plt.show()

Previous_score_corr = df["Previous_Scores"].corr(df["Exam_Score"])
print(f"Correlation: {Previous_score_corr:.2f}")

'''Previous scores show only a weak positive relationship (r = 0.18) with 
current exam scores. Although students with higher previous scores tend to 
perform slightly better, previous academic performance alone is not a strong 
predictor of final exam performance.'''

# Teacher quality
teacher_avg=df.groupby("Teacher_Quality")["Exam_Score"].mean()
print(teacher_avg)
plt.bar(teacher_avg.index,teacher_avg.values,color='orange',edgecolor='black')
plt.title("Teacher quality vs exam score",color="purple",fontsize=15)
plt.xlabel("Teacher quality",color="purple",fontsize=15)
plt.ylabel("avg Exam scores",color="purple",fontsize=15)
plt.grid(alpha=0.6)
plt.savefig("teacher quality.png")
plt.tight_layout()
plt.show()
'''Teacher quality does not show a strong relationship with exam scores in this dataset.
Students taught by high-quality teachers achieved slightly higher average exam scores
than students taught by medium- or low-quality teachers. However, the differences between 
the three groups are very small, indicating that teacher quality alone is not a
major factor influencing exam performance in this dataset.'''

# Average Exam Score by Motivation Level

motivation_avg = df.groupby("Motivation_Level")["Exam_Score"].mean()
print(motivation_avg)

plt.bar(motivation_avg.index,motivation_avg.values,color=["crimson","gold","limegreen"])
plt.title("Average Exam Score by Motivation Level")
plt.xlabel("Motivation Level")
plt.ylabel("Average Exam Score")
plt.grid(axis="y", alpha=0.3)
plt.savefig("motivation level.png")
plt.tight_layout()
plt.show()
'''Students with different motivation levels achieved very similar average exam scores. 
Although highly motivated students scored slightly higher on average, 
the difference between motivation groups is small, suggesting that motivation level alone 
is not a strong predictor of exam performance in this dataset.'''

# does family income have an impact on exam scores
income_avg=df.groupby("Family_Income")["Exam_Score"].mean()
print(income_avg)

plt.bar(income_avg.index,income_avg.values,color=["tomato","gold","limegreen"])
plt.title("Average Exam Score by Family Income")
plt.xlabel("Family Income")
plt.ylabel("Average Exam Score")
plt.grid(axis="y", alpha=0.3)
plt.savefig("family income.png")
plt.tight_layout()
plt.show()
'''Students from high-income families achieved slightly higher average exam scores
than students from medium- and low-income families. However, the differences between 
the groups are relatively small (around one mark), indicating that family income 
alone is not a strong predictor of academic performance in this dataset.'''

# Does internet access influence students' exam performance?
# Average Exam Score by Internet Access

internet_avg = df.groupby("Internet_Access")["Exam_Score"].mean()
print(internet_avg)

plt.bar(internet_avg.index,internet_avg.values,color=["tomato", "dodgerblue"])
plt.title("Average Exam Score by Internet Access",color="purple",fontsize=16)
plt.xlabel("Internet Access",color="olive",fontsize=13)
plt.ylabel("Average Exam Score",color="olive",fontsize=13)
plt.grid(axis="y", alpha=0.3)
plt.savefig("internet access.png")
plt.tight_layout()
plt.show()
'''Students with internet access achieved slightly higher average exam scores than students
without internet access. However, the difference is less than one mark, suggesting that
internet access alone is not strongly associated with exam performance in this dataset.'''

# Learning disabilities vs exam score

# Average Exam Score by Learning Disabilities

ld_avg = df.groupby("Learning_Disabilities")["Exam_Score"].mean()
print(ld_avg)

plt.bar(ld_avg.index,ld_avg.values,color=["tomato","royalblue"])
plt.title("Average Exam Score by Learning Disabilities",color="purple",fontsize=15)
plt.xlabel("Learning Disabilities",color="olive",fontsize=13)
plt.ylabel("Average Exam Score",color="olive",fontsize=13)
plt.grid(axis="y", alpha=0.3)
plt.savefig("learning disabilities.png")
plt.tight_layout()
plt.show()
'''Students with and without learning disabilities achieved similar average exam scores, 
with only a small difference of approximately one mark. This suggests that
learning disabilities alone are not strongly associated with exam performance 
in this dataset.'''

# Average Exam Score by Gender

gender_avg = df.groupby("Gender")["Exam_Score"].mean()
print(gender_avg)

plt.bar(gender_avg.index,gender_avg.values,color=["steelblue","hotpink"])
plt.title("Average Exam Score by Gender",color="purple",fontsize=15)
plt.xlabel("Gender",color="olive",fontsize=13)
plt.ylabel("Average Exam Score",color="olive",fontsize=13)
plt.grid(axis="y", alpha=0.3)
plt.savefig("gender.png")
plt.tight_layout()
plt.show()
'''Male and female students achieved nearly identical average exam scores. 
This suggests that gender is not associated with meaningful differences in 
academic performance within this dataset.'''