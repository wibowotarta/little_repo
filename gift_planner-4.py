# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: GiftPlanner
def edit_gift(gift_id: int, updates: dict) -> GiftRecord | None:
    with open("gifts.json", "r", encoding="utf-8") as f:
        records = json.load(f)
    
    for record in records["records"]:
        if record["id"] == gift_id:
            record.update(updates)
            return record
    
    return None

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 2:
        gift_id = int(sys.argv[1])
        updates_str = " ".join(sys.argv[2:])
        try:
            updates = {k.strip(): v for k, v in [item.split("=", 1) for item in updates_str.split()]}
        except ValueError as e:
            print(f"Ошибка парсинга аргументов: {e}", file=sys.stderr)
            sys.exit(1)
        
        edited = edit_gift(gift_id, updates)
        if edited:
            print(json.dumps(edited, ensure_ascii=False))
        else:
            print("Запись не найдена", file=sys.stderr)
    else:
        print("Использование: python gift_planner.py <id> key=value ...")
