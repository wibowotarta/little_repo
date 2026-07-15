# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: GiftPlanner
def print_gift_record(record):
    """Компактный вывод одной записи планировщика подарков."""
    name = record.get("name", "Без имени")
    occasion = record.get("occasion", "Без повода")
    budget = record.get("budget", 0)
    status = record.get("status", "Не выбрано")
    
    if isinstance(budget, float):
        budget_str = f"{budget:.2f}"
    else:
        budget_str = str(budget)
        
    print(f"🎁 Подарок для {name}")
    print(f"   Повод: {occasion}")
    print(f"   Бюджет: {budget_str} $")
    print(f"   Статус: {status}")
    
    if "gift_idea" in record and record["gift_idea"]:
        idea = record["gift_idea"]
        print(f"   💡 Идея: {idea}")

# Пример использования
sample_record = {
    "name": "Анна",
    "occasion": "День рождения",
    "budget": 150.75,
    "status": "Куплено",
    "gift_idea": "Сертификат на спа-салон"
}

print_gift_record(sample_record)
