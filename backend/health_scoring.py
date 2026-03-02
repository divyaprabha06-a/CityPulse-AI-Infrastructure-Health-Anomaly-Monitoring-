def calculate_health_score(issues, anomaly):
    score = 100
    score -= len(issues) * 15

    if anomaly == 1:
        score -= 25

    score = max(score, 0)

    if score >= 80:
        status = "Healthy"
    elif score >= 50:
        status = "Warning"
    else:
        status = "Critical"

    return score, status
