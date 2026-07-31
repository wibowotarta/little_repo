# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: GiftPlanner
TEMPLATES = {
    "birthday": {"recipient_name": "Имя", "occasion": "День рождения", "budget": 2000, "status": "planning"},
    "new_year": {"recipient_name": "Имя", "occasion": "Новый год", "budget": 3000, "status": "planning"},
    "anniversary": {"recipient_name": "Имя", "occasion": "Юбилей", "budget": 5000, "status": "planning"},
}

def create_from_template(name, recipient="Анна", occasion=None, budget=None):
    if name not in TEMPLATES:
        print(f"Неизвестный шаблон: {name}")
        return None
    entry = dict(TEMPLATES[name])
    entry["recipient_name"] = recipient or entry.get("recipient_name")
    if occasion is not None:
        entry["occasion"] = occasion
    else:
        entry["occasion"] = entry.get("occasion")
    if budget is not None:
        entry["budget"] = budget
    else:
        entry["budget"] = entry.get("budget")
    return entry

def list_templates():
    print("Доступные шаблоны:")
    for name in TEMPLATES:
        print(f"  - {name}: повод={TEMPLATES[name]['occasion']}, бюджет={TEMPLATES[name]['budget']}")
