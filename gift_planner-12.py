# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: GiftPlanner
import json, os, sys

def load_data(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if not isinstance(data, list):
            print("Ошибка: JSON должен содержать массив объектов.")
            return None
        for i, item in enumerate(data):
            required_keys = {'recipient', 'occasion', 'budget', 'status'}
            missing = required_keys - set(item.keys())
            if missing:
                print(f"Предупреждение: запись {i+1} ({item.get('recipient', 'unknown')}) не содержит ключей: {missing}")
        return data
    except FileNotFoundError:
        print(f"Ошибка: файл '{file_path}' не найден.")
        return None
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}")
        return None

if __name__ == "__main__":
    file_name = sys.argv[1] if len(sys.argv) > 1 else "gifts.json"
    loaded_gifts = load_data(file_name)
    if loaded_gifts is not None:
        print(f"Загружено {len(loaded_gifts)} записей.")
