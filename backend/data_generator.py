import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_sensor_data():
    data = []
    start_time = datetime.now() - timedelta(days=2)

    for asset in range(1, 6):
        time = start_time
        for _ in range(48):
            data.append([
                time,
                f"SL-{asset}",
                np.random.normal(230, 10),
                np.random.normal(1.5, 0.3),
                np.random.normal(45, 8),
                np.random.normal(0.3, 0.1),
                np.random.uniform(0.9, 1.0)
            ])
            time += timedelta(hours=1)

    df = pd.DataFrame(data, columns=[
        "timestamp", "asset_id", "voltage",
        "current", "temperature", "vibration", "uptime"
    ])

    df.to_csv("data/raw/simulated_sensor_data.csv", index=False)
    return df
