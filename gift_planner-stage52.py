# === Stage 52: Добавь экспорт краткого отчёта в текстовом формате ===
# Project: GiftPlanner
def export_report(contacts, occasions, budgets, statuses):
    """Export a short text report to a file."""
    lines = []
    lines.append("=== GiftPlanner Report ===")
    lines.append(f"Total contacts: {len(contacts)}")
    lines.append(f"Total occasions: {len(occasions)}")
    lines.append(f"Total budgets: {len(budgets)}")
    lines.append(f"Total statuses: {len(statuses)}")
    lines.append("")
    lines.append("--- Contacts ---")
    for name, email, phone in contacts:
        lines.append(f"  {name}: {email}, {phone}")
    lines.append("")
    lines.append("--- Occasions ---")
    for occasion in occasions:
        lines.append(f"  {occasion}")
    lines.append("")
    lines.append("--- Budgets ---")
    for budget in budgets:
        lines.append(f"  {budget}")
    lines.append("")
    lines.append("--- Statuses ---")
    for status in statuses:
        lines.append(f"  {status}")
    with open("gift_report.txt", "w") as f:
        f.write("\n".join(lines))
    return "Report exported to gift_report.txt"
