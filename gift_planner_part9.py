# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: GiftPlanner
import json, sys
from pathlib import Path

def load_initial_data(json_string: str) -> dict[str, list]:
    """Парсит JSON-строку в структуру данных проекта."""
    try:
        data = json.loads(json_string)
        if not isinstance(data, dict):
            raise ValueError("JSON должен содержать объект (dict).")
        
        # Валидация обязательных полей
        required_keys = {"recipients", "occasions"}
        missing = required_keys - set(data.keys())
        if missing:
            raise KeyError(f"Отсутствуют ключи: {missing}")
        
        # Проверка типов данных для списков
        for key in ["recipients", "occasions"]:
            if not isinstance(data[key], list):
                raise TypeError(f"Поле '{key}' должно быть списком.")
            
            # Валидация элементов списка (пример)
            for item in data[key]:
                if not isinstance(item, dict):
                    raise ValueError(f"Элемент в списке '{key}' должен быть словарем.")

        return data
        
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Неожиданная ошибка при загрузке данных: {e}", file=sys.stderr)
        sys.exit(1)

# Пример использования (раскомментируйте для теста):
if __name__ == "__main__":
    sample_json = '''
    {
        "recipients": [
            {"id": 1, "name": "Анна", "birthday": "2024-12-25"},
            {"id": 2, "name": "Иван", "birthday": "2024-12-30"}
        ],
        "occasions": [
            {"id": 1, "title": "День рождения Анны", "date": "2024-12-25"},
            {"id": 2, "title": "Новый год", "date": "2024-12-31"}
        ]
    }'''
    
    # Загрузка данных из строки
    initial_data = load_initial_data(sample_json)
    print(f"Загружено {len(initial_data['recipients'])} получателей и {len(initial_data['occasions'])} поводов.")
