# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: GiftPlanner
def print_metrics(data):
    if not data:
        return "Нет данных для анализа."
    
    total = len(data)
    spent_total = sum(item['spent'] for item in data if 'spent' in item)
    budget_total = sum(item.get('budget', 0) for item in data)
    avg_spent = spent_total / total if total else 0
    
    statuses = set()
    for item in data:
        if 'status' in item:
            statuses.add(item['status'])
    
    status_counts = {s: sum(1 for i in data if i.get('status') == s) for s in statuses}
    most_common_status = max(status_counts, key=status_counts.get) if status_counts else "Неизвестный"
    
    print(f"Всего записей: {total}")
    print(f"Общий бюджет: {budget_total:.2f}")
    print(f"Расход: {spent_total:.2f} (среднее на запись: {avg_spent:.2f})")
    print(f"Статусы: {dict(status_counts)} (основной: {most_common_status})")
