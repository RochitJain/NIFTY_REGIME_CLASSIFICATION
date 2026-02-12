import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import numpy as np

df = yf.download("^NSEI", start="2012-01-01", end="2026-01-31")
df.columns = df.columns.get_level_values(0)

# print(df.index.min(), df.index.max())

df["MA_20"] = df["Close"].rolling(20).mean()
df["MA_50"] = df["Close"].rolling(50).mean()
# print(df[["Close", "MA_20", "MA_50"]].head(60))

# plt.figure(figsize=(12,6))
# plt.plot(df["Close"], label="Close")
# plt.plot(df["MA_20"], label="MA 20")
# plt.plot(df["MA_50"], label="MA 50")
# plt.legend()
# plt.show()
# print(df.head())
# print(df.shape)
# df["trend_signal"] = df["MA_20"] > df["MA_50"]

# print(df["trend_signal"].value_counts())

condition = [
    (df["MA_20"] > df["MA_50"]) & (df["Close"]> df["MA_20"]),
    (df["MA_20"] < df["MA_50"]) & (df["Close"]< df["MA_20"])
]
choices = ["Upward", "Downward"]

df["trend"] = np.select(condition, choices,default="Sideways")

print(df["trend"].value_counts(normalize=True))

print(df["trend"].value_counts())

# df["return_5"] = df["Close"].pct_change(5)
# df["vol_20"] = df["Close"].rolling(20).std()
# df["dist_ma20"] = df["Close"] - df["MA_20"]
# df[["return_5","vol_20","dist_ma20"]].describe()