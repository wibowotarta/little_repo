# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: GiftPlanner
def migrate_gift_planner_data():
    """Миграция структуры данных GiftPlanner: добавление полей для расширенной поддержки."""
    schema_version = 46
    print(f"Выполняется миграция GiftPlanner: версия {schema_version}")

    # Добавляем поля для хранения истории подарков и уведомлений
    new_fields = {
        "gift_history": [],
        "notifications": [],
        "preferences": {
            "preferred_categories": [],
            "budget_alerts": []
        }
    }

    # Проверяем, что текущая версия данных устарела
    current_version = get_current_version()
    if current_version < schema_version:
        print("Обнаружена устаревшая версия данных. Запуск миграции...")
        update_data_fields(new_fields)
        print("Миграция завершена успешно.")
        return True
    else:
        print("Данные уже актуальны. Миграция не требуется.")
        return False

    def get_current_version():
        """Получение текущей версии данных."""
        return 40  # Пример текущей версии

    def update_data_fields(new_fields):
        """Обновление полей данных."""
        current_data = get_current_data()
        current_data.update(new_fields)
        save_current_data(current_data)

    def get_current_data():
        """Получение текущих данных."""
        return {"version": 40}

    def save_current_data(data):
        """Сохранение обновленных данных."""
        print(f"Данные обновлены и сохранены. Текущая версия: {data['version']}")
