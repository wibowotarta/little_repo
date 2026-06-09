# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: GiftPlanner
def init_demo_data():
    recipients = [
        {"name": "Анна", "birthday": "2024-12-25", "reason": "День рождения", "budget_max": 3000, "status": "planned"},
        {"name": "Иван", "birthday": "2024-12-26", "reason": "Новый год", "budget_max": 5000, "status": "planned"},
        {"name": "Мария", "birthday": "2024-12-30", "reason": "Рождение ребенка", "budget_max": 10000, "status": "planned"}
    ]
    gifts = [
        {"recipient_id": 0, "item": "Книги", "price": 1500, "status": "ordered"},
        {"recipient_id": 1, "item": "Подушка-грелка", "price": 2500, "status": "planned"}
    ]
    print("Демо-данные инициализированы.")
    return recipients, gifts

if __name__ == "__main__":
    init_demo_data()
