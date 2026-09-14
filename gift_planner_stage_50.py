# === Stage 50: Сделай аккуратную финальную полировку сообщений, названий функций и комментариев ===
# Project: GiftPlanner
def polish_gift_planner():
    """Финальная полировка: выводит отформатированный список всех подарков с статусами."""
    print("=" * 60)
    print("🎁 GIFT PLANNER — ОБЗОР ВСЕХ ПОДАРКОВ")
    print("=" * 60)
    for gift in all_gifts:
        status_icon = "✅" if gift["status"] == "bought" else "🔲" if gift["status"] == "planned" else "📋"
        print(f"{status_icon} {gift['recipient']:15} | {gift['occasion']:20} | Бюджет: {gift['budget']}₽ | Статус: {gift['status']}")
    print("=" * 60)
    return all_gifts
