# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: GiftPlanner
def generate_summary():
    if not recipients: return print("Нет данных.")
    total_budget = sum(r.budget for r in recipients)
    spent = sum(bought.price or 0 for bought in gifts.values())
    remaining = total_budget - spent
    status_counts = {}
    for g in gifts.values():
        s = g.status.value if hasattr(g, 'status') else str(g.status)
        status_counts[s] = status_counts.get(s, 0) + 1
    print(f"Сводка: {len(recipients)} получателей, бюджет {total_budget:.2f}, потрачено {spent:.2f}, осталось {remaining:.2f}")
    for s, count in sorted(status_counts.items()):
        print(f"Статус '{s}': {count} подарков")
