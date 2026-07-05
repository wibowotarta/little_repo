# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: GiftPlanner
def archive_old_records(archive_days=365):
    from datetime import datetime, timedelta
    cutoff = datetime.now() - timedelta(days=archive_days)
    archived_count = 0
    for gift in gifts:
        if gift['status'] == 'bought' and gift['purchased_at']:
            purchased_dt = datetime.strptime(gift['purchased_at'], '%Y-%m-%d')
            if purchased_dt < cutoff:
                gift['archived'] = True
                archived_count += 1
    return archived_count
