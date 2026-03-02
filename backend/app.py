import pandas as pd
from backend.data_generator import generate_sensor_data
from backend.rule_engine import apply_rules
from backend.anomaly_detection import detect_anomalies
from backend.health_scoring import calculate_health_score
from backend.alert_service import send_alert

def main():
    df = generate_sensor_data()
    df = detect_anomalies(df)

    results = []

    for _, row in df.iterrows():
        issues = apply_rules(row)
        score, status = calculate_health_score(issues, row["anomaly"])

        results.append([
            row["timestamp"],
            row["asset_id"],
            score,
            status,
            issues
        ])

        send_alert(row["asset_id"], status, issues)

    result_df = pd.DataFrame(results, columns=[
        "timestamp", "asset_id",
        "health_score", "health_status", "issues"
    ])

    result_df.to_csv("data/processed/health_report.csv", index=False)
    print("✅ Health report generated")

if __name__ == "__main__":
    main()
