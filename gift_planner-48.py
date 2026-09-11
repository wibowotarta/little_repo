# === Stage 48: Проведи рефакторинг: разнеси крупные функции, сохрани совместимость публичных команд ===
# Project: GiftPlanner
def get_status_label(status):
    """Converts a status string to a readable label."""
    labels = {
        'pending': 'Ожидается',
        'ordered': 'Заказан',
        'shipped': 'Доставлен',
        'received': 'Получен',
        'cancelled': 'Отменен'
    }
    return labels.get(status, status)
