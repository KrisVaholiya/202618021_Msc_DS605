# DS605 Lab Assignment 3

## Scikit-learn: Data Preprocessing and Model Performance Evaluation

### Student Information

- **Name:** Kris Jagdishbhai Vaholiya
- **Student ID:** 202618021
- **Course:** DS605 - Fundamentals of Machine Learning
- **Lab Assignment:** 3

---

## Objective

The objective of this assignment is to build and compare Scikit-learn preprocessing pipelines and evaluate two classification models for predicting whether a hotel booking will be canceled.

The assignment compares:

1. Logistic Regression with StandardScaler
2. Logistic Regression with MinMaxScaler
3. Decision Tree with StandardScaler
4. Decision Tree with MinMaxScaler

---

## Dataset

**Dataset:** Hotel Booking Demand

The dataset used in this assignment is:

- `hotel_bookings.csv`
- Source: Kaggle Hotel Booking Demand dataset

The target variable is:

- `is_canceled`
  - `0` = Booking was not canceled
  - `1` = Booking was canceled

---

## Project Structure

```text
DS605_Lab3/
│
├── DS605_Lab3_Hotel_Booking_Assignment.ipynb
├── hotel_bookings.csv
├── cleaned_hotel_bookings.csv        # Optional/generated after cleaning
└── README.md
```

---

## Data Preprocessing

The following preprocessing steps were performed:

### 1. Data Exploration

The dataset was examined using:

- `head()`
- `shape`
- `info()`
- `describe()`
- `dtypes`
- Class distribution of `is_canceled`

### 2. Missing Values

Missing values were identified by calculating:

- Missing value count
- Missing value percentage

For numerical features:

- `KNNImputer(n_neighbors=5)` was used.

For categorical features:

- `SimpleImputer(strategy="most_frequent")` was used.

### 3. Data Leakage Removal

The following columns were removed because they can reveal information about the final booking outcome:

- `reservation_status`
- `reservation_status_date`

Columns with extremely high missingness were also considered for removal.

### 4. Outlier Detection

Selected numerical features were checked for extreme outliers using boxplots and the IQR method.

A conservative `3 × IQR` rule was used to remove only clear or extreme outliers.

### 5. Feature Transformation

Numerical and categorical features were processed separately using `ColumnTransformer`.

Categorical features were transformed using:

```python
OneHotEncoder(handle_unknown="ignore")
```

---

## Preprocessing Pipelines

### Pipeline A

Numerical features:

```text
KNNImputer → StandardScaler
```

Categorical features:

```text
SimpleImputer → OneHotEncoder
```

### Pipeline B

Numerical features:

```text
KNNImputer → MinMaxScaler
```

Categorical features:

```text
SimpleImputer → OneHotEncoder
```

The preprocessing pipelines were fitted only on the training data using Scikit-learn `Pipeline` and `ColumnTransformer`.

---

## Train-Test Split

The dataset was split using:

```python
train_test_split(
    test_size=0.2,
    stratify=y,
    random_state=42
)
```

The same train-test split was used for all four experiments.

---

## Models

Two classification models were used.

### Logistic Regression

```python
LogisticRegression(max_iter=1000)
```

### Decision Tree

```python
DecisionTreeClassifier(random_state=42)
```

This produced four model-pipeline combinations:

| Model | Preprocessing Pipeline |
|---|---|
| Logistic Regression | Pipeline A - StandardScaler |
| Logistic Regression | Pipeline B - MinMaxScaler |
| Decision Tree | Pipeline A - StandardScaler |
| Decision Tree | Pipeline B - MinMaxScaler |

---

## Evaluation Metrics

Each experiment was evaluated using:

- Training Accuracy
- Testing Accuracy
- Precision
- Recall
- F1-Score

The train-test accuracy difference was also used to identify possible overfitting.

Confusion matrices were created for:

1. The best Logistic Regression model
2. The best Decision Tree model

---

## Results

Run the Jupyter Notebook to generate the final performance comparison table.

The table compares all four model-pipeline combinations using training accuracy, testing accuracy, precision, recall, and F1-score.

### Final Comparison Table

After running the notebook, paste or generate the results here:

| Model + Pipeline | Training Accuracy | Testing Accuracy | Precision | Recall | F1-Score |
|---|---:|---:|---:|---:|---:|
| Logistic Regression + Pipeline A | | | | | |
| Logistic Regression + Pipeline B | | | | | |
| Decision Tree + Pipeline A | | | | | |
| Decision Tree + Pipeline B | | | | | |

---

## Final Observations

After running the notebook, update these observations using your actual results:

1. The model with the highest testing performance and F1-score is considered the best overall model.
2. Logistic Regression may be affected by the choice between StandardScaler and MinMaxScaler because it is sensitive to feature scale.
3. Decision Trees are generally less sensitive to feature scaling than Logistic Regression.
4. A large difference between training and testing accuracy can indicate possible overfitting.
5. The confusion matrices provide additional information about how accurately the best models classify canceled and non-canceled bookings.

---

## Technologies and Libraries Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook

---

## How to Run

1. Download or clone this repository.
2. Place `hotel_bookings.csv` in the project folder.
3. Open `DS605_Lab3_Hotel_Booking_Assignment.ipynb`.
4. Run all cells from top to bottom.
5. The notebook will generate:
   - Data exploration results
   - Missing value analysis
   - Preprocessing pipelines
   - Four trained model combinations
   - Performance comparison table
   - Confusion matrices
   - Final observations

---

## Submission

The assignment requires a public GitHub repository containing:

- Complete runnable Jupyter Notebook
- `README.md`
- Dataset or cleaned base dataset used for modeling, if required
- Final comparison table
- Required confusion matrix figures

Only the public GitHub repository link should be submitted.
