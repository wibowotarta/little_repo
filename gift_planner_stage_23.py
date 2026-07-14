# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: GiftPlanner
def print_gift_table(gifts):
    """Compact console table of all gift records."""
    if not gifts:
        print("Список подарков пуст")
        return
    headers = ["ID", "Получатель", "Повод", "Статус", "Бюджет"]
    widths = [len(h) for h in headers]
    lines = []
    for i, g in enumerate(gifts):
        row = [str(i+1), g.get('recipient', ''), g.get('occasion', ''),
               g.get('status', ''), g.get('budget', '')]
        line = " | ".join(r.ljust(widths[j]) for j, r in enumerate(row))
        lines.append(line)
    max_w = max(len(l) for l in lines) + 2
    print("-" * max_w)
    print(" | ".join(h.ljust(widths[j]) for j, h in enumerate(headers)))
    print("-" * max_w)
    for line in lines:
        print(line)
    print("-" * max_w)
