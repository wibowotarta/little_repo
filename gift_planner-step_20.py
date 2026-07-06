# === Stage 20: Добавь восстановление записей из архива ===
# Project: GiftPlanner
def load_from_archive(archive_path):
    """Восстанавливает записи из архива, имитируя чтение JSON."""
    records = []
    try:
        with open(archive_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                record = json.loads(line)
                records.append(record)
            print(f"[Archive] Loaded {len(records)} records from '{archive_path}'.")
    except FileNotFoundError:
        print("[Archive] File not found. Nothing to restore.")
    return records
