# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: GiftPlanner
def test_gift_planner_basic():
    from gift_planner import GiftPlanner
    planner = GiftPlanner()
    assert planner.add_recipient("Alice") == "Alice"
    assert planner.add_occasion("Birthday", budget=100) == "Birthday"
    assert planner.add_gift("Alice", "Birthday", "Book", 40, "Purchased") == "Purchased"
    assert planner.get_report() == "Alice's Birthday: Book (40) - Purchased"
    assert planner.get_summary() == "1 recipient, 1 occasion, 1 gift, 1 purchased"
