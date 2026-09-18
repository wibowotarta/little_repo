# === Stage 53: Добавь импорт отчёта или списка записей из простого текстового формата ===
# Project: GiftPlanner
def export_records(path, records=None):
    """Export a list of records to a simple text file (CSV-like)."""
    if records is None:
        records = []
    if not records:
        with open(path, 'w', encoding='utf-8') as f:
            f.write('No records to export.\n')
        return
    lines = []
    for r in records:
        line = ','.join(str(getattr(r, f) or '') for f in ['recipient', 'occasion', 'budget', 'status'])
        lines.append(line)
    with open(path, 'w', encoding='utf-8') as f:
        f.write('recipient,occasion,budget,status\n')
        f.write('\n'.join(lines) + '\n')
    print(f'Records exported to {path}')
