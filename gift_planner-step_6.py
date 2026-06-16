# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: GiftPlanner
def filter_gifts(status=None, category=None, tags=None):
    filtered = []
    for gift in gifts:
        if status and gift['status'] != status: continue
        if category and gift.get('category') != category: continue
        if tags and not any(tag in gift.get('tags', []) for tag in tags.split()): continue
        filtered.append(gift)
    return filtered

def search_gifts(query):
    results = []
    query_lower = query.lower()
    for gift in gifts:
        text = f"{gift['name']} {gift['recipient']['name']}".lower()
        if query_lower in text or any(query_lower in tag for tag in gift.get('tags', [])):
            results.append(gift)
    return results

def get_summary():
    total_budget = sum(g['budget'] for g in gifts)
    spent = sum(g['spent'] for g in gifts if g['status'] == 'bought')
    pending = len([g for g in gifts if g['status'] != 'bought'])
    return {'total': total_budget, 'spent': spent, 'pending_count': pending}
