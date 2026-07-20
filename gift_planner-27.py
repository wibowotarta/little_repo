# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: GiftPlanner
def reset_demo_data():
    """Сбрасывает все данные в дефолтные значения для тестирования."""
    global recipients, occasions, budget, status_options
    recipients = [
        {"id": 1, "name": "Анна", "age": 28},
        {"id": 2, "name": "Борис", "age": 35},
        {"id": 3, "name": "Виктория", "age": 42},
    ]
    occasions = [
        {"id": 1, "occasion": "День рождения"},
        {"id": 2, "occasion": "Новый год"},
        {"id": 3, "occasion": "8 марта"},
    ]
    budget = 5000
    status_options = ["Не куплено", "В процессе поиска", "Куплено"]
    print("Демо-данные сброшены.")


def clear_all_data():
    """Полностью очищает все данные и сбрасывает в дефолты."""
    recipients.clear()
    occasions.clear()
    budget = 0
    status_options.clear()
    reset_demo_data()
    print("Все данные полностью очищены и сброшены в дефолты.")


if __name__ == "__main__":
    # Тест сброса демо-данных
    reset_demo_data()
    print(recipients)

    # Тест полной очистки
    clear_all_data()
