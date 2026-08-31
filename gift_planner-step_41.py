# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: GiftPlanner
def dry_run(operation, **kwargs):
    """Execute operation in dry-run mode: log the intended action without persisting it."""
    print(f"[DRY-RUN] {operation} -> {kwargs}")
    return False
