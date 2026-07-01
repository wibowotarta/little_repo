# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: GiftPlanner
def calculate_monthly_stats(records):
    from collections import defaultdict
    stats = defaultdict(lambda: {'count': 0, 'total_budget': 0})
    for r in records:
        date_str = r.get('date') or ''
        if not date_str: continue
        try:
            dt = datetime.strptime(date_str[:10], '%Y-%m-%d')
            key = f"{dt.year}-{dt.month}"
            stats[key]['count'] += 1
            budget = float(r.get('budget', 0))
            status = r.get('status', '').lower()
            if status in ('planned', 'bought'):
                stats[key]['total_budget'] += budget
        except ValueError:
            continue
    return dict(sorted(stats.items()))
