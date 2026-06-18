# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: GiftPlanner
def sort_gifts(gifts, key='date'):
    if not gifts: return []
    
    def parse_date(date_str):
        try:
            parts = date_str.split()
            day = int(parts[0])
            month = int(parts[1].split('-')[0])
            year = int(parts[2][:4])
            return (year, month, day)
        except:
            return (9999, 12, 31)

    def parse_priority(priority_str):
        try:
            p = int(priority_str.replace(' ', ''))
            if p < 0: return -p * 10 + 100
            elif p > 10: return (p - 10) / 2.5
            else: return p
        except:
            return 99

    def parse_name(name):
        try:
            words = name.lower().split()
            if len(words) >= 3 and words[2].isdigit():
                year, month, day = map(int, words[:3])
                return (year, month, day, name)
        except:
            pass
        return ('', '', '', name)

    sort_keys = {
        'date': lambda x: parse_date(x.get('date') or ''),
        'priority': lambda x: parse_priority(x.get('priority') or 0),
        'name': lambda x: (x.get('id') or '').lower(),
        'combined': lambda x: (parse_date(x.get('date') or '')[1], -parse_priority(x.get('priority') or 0), x.get('name', ''))
    }

    key_func = sort_keys.get(key, sort_keys['date'])
    return sorted(gifts, key=key_func)
