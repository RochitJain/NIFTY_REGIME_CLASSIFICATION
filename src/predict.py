import joblib
import yfinance as yf
from src.features import create_feature

MODEL_PATH = "models/model.pkl"
SCALER_PATH = "models/scaler.pkl"

def predict_trend():
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)

    df = yf.download("^NSEI", period="6mo", interval="1d")
    df.columns = df.columns.get_level_values(0)
    df = create_feature(df)

    features = df[[
        "dist_ma20",
        "return_5",
        "vol_20",
        "ma20_slope",
        "volume_ratio"
    ]]

    feature_scaled = scaler.transform(features.iloc[[-1]])
    prediction = model.predict(feature_scaled)
    return prediction[0]
