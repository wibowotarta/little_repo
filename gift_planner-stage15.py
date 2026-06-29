# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: GiftPlanner
def calculate_weekly_stats(gifts):
    from datetime import date, timedelta
    weekly_data = {}
    for gift in gifts:
        if not gift.get('date'): continue
        d = date.fromisoformat(gift['date'])
        week_start = (d - timedelta(days=d.weekday())).isoformat()
        key = f"{week_start}+{gift.get('reason', 'unknown')}:{gift.get('recipient_name', '')}"
        weekly_data[key] = weekly_data.get(key, 0) + gift.get('cost', 0)
    return sorted(weekly_data.items(), key=lambda x: x[1], reverse=True)[:5]
