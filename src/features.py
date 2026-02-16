def create_feature(df):
    df["MA_20"] = df["Close"].rolling(20).mean()
    df["MA_50"] = df["Close"].rolling(50).mean()
    df["return_5"] = df["Close"].pct_change(5)
    df["vol_20"] = df["Close"].rolling(20).std()
    df["dist_ma20"] = df["Close"] - df["MA_20"]
    df["ma20_slope"] = df["MA_20"] - df["MA_20"].shift(5)
    df["volume_ratio"] = df["Volume"] / df["Volume"].rolling(20).mean()
    df = df.dropna()
    
    return df