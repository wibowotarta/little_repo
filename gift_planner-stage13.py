# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: GiftPlanner
def search_gifts(query: str, recipients=None, occasions=None, statuses=None):
    query = query.lower().strip()
    results = []
    for gift in gifts:
        match = False
        if not query or (query in gift['recipient_name'].lower()) or \
           (query in gift['occasion'].lower()) or \
           (query in gift['status'].lower()):
            match = True
        if recipients and gift['recipient_id'] not in recipients:
            continue
        if occasions and query.lower() not in [o.lower() for o in gift.get('occasions', [])]:
            continue
        if statuses and gift['status'] != status.upper():
            continue
        results.append(gift)
    return results
