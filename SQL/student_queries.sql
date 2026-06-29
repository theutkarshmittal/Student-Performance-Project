create database student_project;
use student_project;
select * from student_performance limit 10;

-- Avg exam score
select avg(Exam_Score) as "AVG SCORE" from student_performance;

-- students scored above 90
select * from student_performance
where Exam_Score>90;

-- avg score by gender
select Gender , avg(Exam_Score) as "AVG SCORE" from student_performance
group by gender;

-- avg score by family income
select Family_Income,avg(Exam_Score) as "AVG SCORE" from student_performance
group by Family_Income;

-- avg score by motivation level
SELECT Motivation_Level,avg(Exam_Score) AS Average_Score from student_performance
GROUP BY Motivation_Level;

-- top 10 students
select * from student_performance 
order by Exam_Score desc
limit 10;

-- how many students belong to each school type
select count(*) as "Total Students" , School_Type
from student_performance
group by School_Type;

-- avg attendance by gender
select Gender , avg(Attendance) as Average_Attendance from student_performance
group by Gender;

-- Average study hours for students scoring above 80
select avg(Hours_Studied) as "Study Hours" , Exam_Score from student_performance
where Exam_Score>80;

-- Which motivation level has the highest average score?
select Motivation_Level , avg(Exam_Score) as "AVG SCORE" from student_performance
group by Motivation_Level
order by avg(Exam_Score) desc;

-- Find the average exam score for each parental involvement level.
select Parental_Involvement,avg(Exam_Score) as "AVG SCORE" from student_performance
group by Parental_Involvement
order by avg(Exam_Score) desc;

-- Which family income group has the highest number of students scoring above 70?
select count(*) as "Total Students" , Family_Income from student_performance
where Exam_Score>70 group by Family_Income ;

-- Find the average exam score of students whose attendance is above the overall average attendance.
select avg(Exam_Score) as "Avg Score" from student_performance
where Attendance > (select avg(Attendance) from student_performance);

-- Find all students whose exam score is higher than the average exam score.
select * from student_performance 
where Exam_Score > ( select avg(Exam_Score) from student_performance);

-- Rank all students based on their exam score.
select * , row_number() over(order by Exam_Score desc) as "Student Rank" from student_performance;

-- rank boys and girls separately
select * , row_number() over(partition by Gender order by Exam_Score desc )as "Rank"
from student_performance;

-- top 3 students within each gender 
SELECT *
FROM(SELECT *,ROW_NUMBER() OVER(
                PARTITION BY Gender
               ORDER BY Exam_Score DESC ) AS Student_Rank FROM student_performance) AS ranked_students
WHERE Student_Rank <= 3;

-- RANK function
select Gender,Exam_Score,rank() over(order by Exam_Score desc) as "Student Rank" from student_performance

-- Dense Rank
Select Gender,Exam_Score,Dense_Rank() over(order by Exam_Score desc) as "Student Rank" from student_performance


/* Create a CTE named high_scorers that stores all students with Exam_Score > 80,
 then display all records from that CTE.*/
with high_scorers as (select * from student_performance where Exam_Score >80)
select * from high_scorers;

-- Find the average exam score of high scorers (students scoring above 80).
with high_scorers as(select * from student_performance where Exam_Score >80) 
select avg(Exam_Score) as "Avg score" from high_scorers;

-- Create a CTE called high_attendance containing students whose attendance is above 90. 
-- Then display only the Female students from that CTE.

with high_attendance as (select * from student_performance where Attendance > 90) 
select * from high_attendance  where Gender = "Female" ;

-- Find the top 3 students within each gender using a CTE.

WITH top_3_students AS
( SELECT *, DENSE_RANK() OVER( PARTITION BY Gender ORDER BY Exam_Score DESC) AS student_rank
    FROM student_performance
)
SELECT *
FROM top_3_students
WHERE student_rank <= 3;
