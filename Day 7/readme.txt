# 📊 Student Performance Analysis

## 📌 Project Overview

This project analyzes student performance using a real-world CSV dataset. 
The analysis was performed using Python, Pandas, Matplotlib, and Seaborn in Google Colab.

The project focuses on cleaning the dataset, performing basic analysis, creating visualizations, and extracting meaningful insights from student performance data.

---

## 🎯 Objectives

- Load and analyze a real CSV dataset.
- Identify and handle missing values.
- Perform basic statistical analysis.
- Analyze student marks based on city and gender.
- Create different types of data visualizations.
- Extract meaningful insights from the dataset.

---

## 📂 Dataset

The dataset contains information about students, including:

- `Name` – Student name
- `Age` – Student age
- `Gender` – Student gender
- `Marks` – Student marks
- `City` – Student city

---

## 🧹 Data Cleaning

The dataset was checked for missing values.

Missing values were found in:

- Age
- Marks
- City

The missing numerical values were filled using the **median**, while the missing city value was filled using the **mode**.

After cleaning, there were no missing values remaining in the dataset.

---

## 📊 Analysis Performed

The following analysis was performed:

- Average student marks
- Highest student marks
- Lowest student marks
- Average marks by city
- Average marks by gender

### Results

- Average Marks: **81.3**
- Highest Marks: **97**
- Lowest Marks: **55**
- Highest City Average: **Bangalore – 90.63**
- Lowest City Average: **Mysore – 71.25**
- Female Average: **89.3**
- Male Average: **73.3**

---

## 📈 Visualizations

Four visualizations were created:

### 1. Marks Distribution
**Type:** Histogram

Shows the distribution of student marks across different score ranges.

### 2. Average Marks by City
**Type:** Bar Chart

Compares the average marks of students from different cities.

### 3. Average Marks by Gender
**Type:** Bar Chart

Compares the average marks between male and female students.

### 4. Age vs Student Marks
**Type:** Scatter Plot

Shows the relationship between student age and marks.

---

## 💡 Key Insights

1. The overall average marks of students is **81.3**.
2. The highest marks obtained by a student is **97**.
3. The lowest marks obtained by a student is **55**.
4. Bangalore has the highest average marks at **90.63**.
5. Mysore has the lowest average marks at **71.25**.
6. Female students have a higher average score (**89.3**) compared to male students (**73.3**).
7. Bangalore and Dharwad show the strongest average academic performance.

---

## 🛠️ Technologies Used

- Python
- Pandas
- Matplotlib
- Seaborn
- Google Colab
- GitHub

---

## 📁 Project Structure

```text
Student-Performance-Analysis/
│
├── data/
│   └── student_data.csv
│
├── visualizations/
│   ├── marks_distribution.png
│   ├── average_marks_by_city.png
│   ├── average_marks_by_gender.png
│   └── age_vs_marks.png
│
├── Student_Performance_Analysis.ipynb
│
└── README.md
