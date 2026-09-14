
import pandas as pd, numpy as np, joblib, os
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import RandomizedSearchCV

DATA_PATH="data/AB_NYC_2019.csv"
os.makedirs("models",exist_ok=True)
df=pd.read_csv(DATA_PATH)
df=df[df["price"]>0].copy()
upper=df["price"].quantile(.99)
df=df[df["price"]<=upper].copy()
df["last_review"]=pd.to_datetime(df["last_review"],errors="coerce")
df["review_recency_days"]=(pd.Timestamp("2019-07-01")-df["last_review"]).dt.days.clip(lower=0)
df["has_reviews"]=(df["number_of_reviews"]>0).astype(int)
df["reviews_per_month"]=df["reviews_per_month"].fillna(0)

features=["neighbourhood_group","neighbourhood","latitude","longitude","room_type",
"minimum_nights","number_of_reviews","reviews_per_month","calculated_host_listings_count",
"availability_365","review_recency_days","has_reviews"]
X=df[features]; y=df["price"]
cat=["neighbourhood_group","neighbourhood","room_type"]
num=[c for c in features if c not in cat]
pre=ColumnTransformer([
("cat",Pipeline([("imputer",SimpleImputer(strategy="most_frequent")),
("enc",OrdinalEncoder(handle_unknown="use_encoded_value",unknown_value=-1))]),cat),
("num",SimpleImputer(strategy="median"),num)
])
model=Pipeline([("pre",pre),("model",RandomForestRegressor(
n_estimators=90,max_depth=30,min_samples_leaf=4,max_features=0.6,n_jobs=-1,random_state=42))])
Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=.2,random_state=42)
model.fit(Xtr,ytr); pred=model.predict(Xte)
print("MAE:",mean_absolute_error(yte,pred))
print("RMSE:",mean_squared_error(yte,pred)**0.5)
print("R2:",r2_score(yte,pred))
model.fit(X,y)
joblib.dump(model,"models/airbnb_price_pipeline.joblib")
print("Saved models/airbnb_price_pipeline.joblib")
