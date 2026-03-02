def send_alert(asset_id, status, issues):
    if status != "Healthy":
        print("🚨 ALERT")
        print("Asset:", asset_id)
        print("Status:", status)
        print("Issues:", issues)
        print("-----------------------")
