# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: GiftPlanner
def check_expired_reminders(people):
    """Проверяет, есть ли просроченные напоминания о подарках."""
    today = datetime.date.today()
    expired = []
    for person in people:
        if person.get('reminder_date') and isinstance(person['reminder_date'], str):
            reminder = datetime.strptime(person['reminder_date'], '%Y-%m-%d').date()
            if reminder < today and person.get('status') != 'bought':
                expired.append({
                    'name': person['name'],
                    'reason': person.get('occasion', ''),
                    'reminder_date': person['reminder_date']
                })
    return expired
