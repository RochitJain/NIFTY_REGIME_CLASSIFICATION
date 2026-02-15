import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import numpy as np

from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix,classification_report
from sklearn.ensemble import RandomForestClassifier

df = yf.download("^NSEI", start="2012-01-01", end="2026-01-31")
df.columns = df.columns.get_level_values(0)

df["MA_20"] = df["Close"].rolling(20).mean()
df["MA_50"] = df["Close"].rolling(50).mean()
df["volume_ratio"] = df["Volume"] / df["Volume"].rolling(20).mean()

condition = [
    (df["MA_20"] > df["MA_50"]) & (df["Close"]> df["MA_20"]),
    (df["MA_20"] < df["MA_50"]) & (df["Close"]< df["MA_20"])
]
choices = ["Upward", "Downward"]

df["trend"] = np.select(condition, choices,default="Sideways")

df["return_5"] = df["Close"].pct_change(5)
df["vol_20"] = df["Close"].rolling(20).std()
df["dist_ma20"] = df["Close"] - df["MA_20"]
df["ma20_slope"] = df["MA_20"] - df["MA_20"].shift(5)

df = df.dropna()

split_date = "2021-01-01"
train_df = df[df.index <split_date]
test_df = df[df.index >= split_date]

X_train = train_df[["dist_ma20","return_5","vol_20","ma20_slope","volume_ratio"]]
y_train = train_df["trend"]

X_test = test_df[["dist_ma20","return_5","vol_20","ma20_slope","volume_ratio"]]
y_test = test_df["trend"]

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = RandomForestClassifier(n_estimators=200, random_state=92)

model.fit(X_train_scaled,y_train)

y_pred = model.predict(X_test_scaled)


print(classification_report(y_test,y_pred))
print(confusion_matrix(y_test,y_pred))

importance = pd.Series(model.feature_importances_,
                       index=X_train.columns)

print(importance.sort_values(ascending=False))
