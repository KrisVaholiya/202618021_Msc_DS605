# DS605 - Lab 02: NumPy and Pandas

## Assignment Title
Lab 02 - NumPy and Pandas: Titanic Dataset Analysis

## Student Details
Name: Your Name
Student ID: Your ID

## Dataset
Titanic Dataset - train.csv

## Objective
This assignment demonstrates NumPy and Pandas operations for data
inspection, filtering, aggregation, missing-value handling, feature
engineering, pivot tables, and visualization.

## Tasks Completed

### Task 4
- Loaded and inspected Titanic train.csv
- Used head(), tail(), shape, columns, info(), describe()
- Demonstrated loc and iloc

### Task 5
- Applied Boolean filtering
- Analyzed passengers based on age, sex, class, fare, survival,
  travelling status, and embarkation

### Task 6
- Used groupby()
- Calculated survival rates
- Calculated average Age and Fare
- Analyzed Sex-Pclass and Embarked groups

### Task 7
- Identified missing values
- Calculated missing-value percentages
- Imputed Age using mean, median, mode, and random values
- Detected Fare outliers using the IQR method

### Task 8
- Created FamilySize
- Created IsAlone
- Created a Sex-Pclass survival pivot table

### Task 9
- Created a correlation heatmap
- Visualized survival rate by Sex
- Created Age vs Fare visualization
- Reported data-driven observations

## Files

- Titanic_Lab02.ipynb - Complete Jupyter Notebook
- train.csv - Original Titanic dataset
- cleaned_titanic.csv - Cleaned and feature-engineered dataset
- figures/ - Generated visualizations

## Key Observations

1. Female passengers had a higher survival rate than male passengers.
2. Passenger class was strongly associated with survival.
3. First-class passengers generally had higher survival rates than
   lower-class passengers.
4. Fare showed a relationship with passenger class and survival.
5. FamilySize and IsAlone provided additional information about
   passenger travelling patterns.
6. Some Titanic columns contained missing values, particularly Age.
7. Fare contained high-value observations that were identified as
   outliers using the IQR method.