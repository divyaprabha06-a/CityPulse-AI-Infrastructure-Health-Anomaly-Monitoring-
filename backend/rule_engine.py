def apply_rules(row):
    issues = []

    if row["temperature"] > 80:
        issues.append("High Temperature")

    if row["voltage"] < 180 or row["voltage"] > 260:
        issues.append("Voltage Issue")

    if row["vibration"] > 0.8:
        issues.append("High Vibration")

    if row["uptime"] < 0.85:
        issues.append("Low Uptime")

    return issues
