# === Stage 55: Добавь мягкую проверку дубликатов при создании записей ===
# Project: GiftPlanner
def check_duplicates(records, record):
    if not record:
        return True
    for r in records:
        if r.get('name') == record.get('name') and r.get('occasion') == record.get('occasion'):
            return False
    return True
