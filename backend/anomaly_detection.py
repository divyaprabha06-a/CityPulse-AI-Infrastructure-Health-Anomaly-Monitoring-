from sklearn.ensemble import IsolationForest

def detect_anomalies(df):
    features = df[["voltage", "current", "temperature", "vibration", "uptime"]]

    model = IsolationForest(contamination=0.05, random_state=42)
    df["anomaly"] = model.fit_predict(features)
    df["anomaly"] = df["anomaly"].apply(lambda x: 1 if x == -1 else 0)

    return df
