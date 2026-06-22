# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: GiftPlanner
def export_to_json():
    import json
    data = {
        "recipients": recipients,
        "occasions": occasions,
        "gifts": gifts,
        "budgets": budgets,
        "statuses": statuses
    }
    return json.dumps(data, indent=2)
