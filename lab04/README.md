# DS605 Lab Assignment 4 — Airbnb Price Prediction

End-to-end machine learning project for predicting nightly Airbnb prices using the **New York City Airbnb Open Data (2019)** dataset.

## Project structure

```text
airbnb_project/
├── AB_NYC_2019.csv              # Dataset (keep local if repository size is a concern)
├── Airbnb_Price_Prediction.ipynb
├── train_model.py
├── app.py
├── requirements.txt
├── model_results.csv
├── models/
│   └── airbnb_price_pipeline.joblib
└── plots/
    ├── price_distribution.png
    ├── median_price_room_type.png
    ├── median_price_borough.png
    ├── model_rmse.png
    └── model_r2.png
```

## 1. Data analysis and preparation

The original dataset contains 48,895 listings and 16 columns.

Cleaning and preprocessing:
- Removed listings with non-positive prices.
- Removed the most extreme 1% of prices to reduce the effect of severe outliers.
- Converted `last_review` to a date.
- Created `review_recency_days` using July 1, 2019 as the dataset reference date.
- Created `has_reviews`.
- Filled missing `reviews_per_month` with 0.
- Used median imputation for numeric variables and most-frequent imputation for categorical variables.
- Used ordinal encoding for categorical variables with unknown-category handling.

Selected predictors:
`neighbourhood_group`, `neighbourhood`, `latitude`, `longitude`, `room_type`, `minimum_nights`, `number_of_reviews`, `reviews_per_month`, `calculated_host_listings_count`, `availability_365`, `review_recency_days`, and `has_reviews`.

## 2. Model comparison

An 80/20 train-test split with `random_state=42` was used.

| Model | MAE ($) | RMSE ($) | R² |
|---|---:|---:|---:|
| Ridge | 50.12 | 79.99 | 0.412 |
| Random Forest | 44.57 | 72.12 | 0.522 |
| Extra Trees | 44.24 | 72.21 | 0.521 |
| **Tuned Random Forest** | **43.98** | **71.58** | **0.529** |

The tuned Random Forest was selected because it achieved the lowest test MAE/RMSE and highest R² among the evaluated models.

### Hyperparameters

- `n_estimators = 90`
- `max_depth = 30`
- `min_samples_leaf = 4`
- `max_features = 0.6`
- `random_state = 42`

A small randomized search with 3-fold cross-validation was used for tuning.

## 3. Interpretation

The model explains about **52.9% of the variation in held-out listing prices**. Its MAE is approximately **$44/night**, meaning predictions are typically off by around $44 in absolute terms on this test set.

Important price-related patterns include:
- Entire homes/apartments generally command higher prices than private or shared rooms.
- Manhattan generally has higher listing prices than the other boroughs.
- Location (latitude/longitude and neighbourhood) is highly informative.
- Minimum-night requirements, availability, reviews, and host listing count provide additional information.

## 4. Streamlit application

Run locally:

```bash
pip install -r requirements.txt
streamlit run app.py
```

The application accepts borough, neighbourhood, room type, geographic coordinates, minimum nights, review information, host listing count, availability, and review recency, then returns an estimated nightly price.

## 5. Deployment

Recommended deployment: **Streamlit Community Cloud**.

1. Push this repository to GitHub.
2. Open Streamlit Community Cloud.
3. Select the GitHub repository.
4. Set the main file to `app.py`.
5. Deploy.
6. Add the resulting public URL below.

**Live application:** _Add your Streamlit URL here after deployment._

## 6. Limitations

- The data represents the NYC Airbnb market in 2019, so current prices may differ substantially.
- The target distribution is strongly right-skewed and contains influential high-price listings.
- The model does not include text/image information, exact amenities, seasonality beyond the available fields, or real-time demand.
- A prediction should be treated as an estimate rather than a guaranteed market price.
- Removing the highest 1% of prices improves robustness but means the model is not designed for extreme luxury listings.

## Reproducibility

To retrain:

```bash
python train_model.py
```

The script evaluates the model on a fixed 20% test set and then fits the selected pipeline on the full cleaned dataset before saving it to `models/airbnb_price_pipeline.joblib`.
