# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: GiftPlanner
import json, datetime
def backup_data():
    try:
        with open("gifts.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {"recipients": [], "occasions": [], "gifts": [], "budgets": [], "purchases": []}
    backup_file = "gifts_backup_" + datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    with open(backup_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Backup saved to {backup_file}")
    return backup_file

if __name__ == "__main__":
    backup_data()
