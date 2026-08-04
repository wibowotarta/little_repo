# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: GiftPlanner
def check_and_repair_data(data):
    """Проверяет целостность данных и пытается исправить простые проблемы:
       - удаляет дубликаты получателей (по email);
       - исправляет статусы 'bought' без бюджета;
       - заполняет пустые поводы из списка типовых."""
    
    reasons = ["birthday", "wedding", "graduation", "anniversary", 
               "new_year", "valentines_day", "christmas", "baby_shower"]
    
    repaired = {k: v.copy() for k, v in data.items()} if isinstance(data, dict) else {}
    
    seen_emails = set()
    repaired_list = []
    
    for item in repaired.values():
        email = item.get("email") or ""
        if email.lower() in seen_emails:
            continue
        seen_emails.add(email.lower())
        
        status = item.get("status", "planned").lower().strip()
        budget = item.get("budget")
        
        if status == "bought" and (not budget or budget <= 0):
            item["budget"] = 1.0
        
        reason = item.get("reason")
        if not reason:
            for r in reasons:
                if r.lower() in email.lower():
                    item["reason"] = r
                    break
        
        repaired_list.append(item)
    
    return repaired_list
