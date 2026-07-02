# === Stage 17: Добавь группировку записей по категориям ===
# Project: GiftPlanner
def group_by_category(records):
    from collections import defaultdict
    grouped = defaultdict(list)
    for rec in records:
        cat = rec.get('category', 'Other') or 'Other'
        grouped[cat].append(rec)
    return dict(sorted(grouped.items()))
