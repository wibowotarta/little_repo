# === Stage 47: Добавь финальную функцию demo(), которая показывает основной пользовательский сценарий ===
# Project: GiftPlanner
def demo():
    """Демонстрация основного сценария GiftPlanner."""
    planner = GiftPlanner()

    # Добавляем получателей
    planner.add_recipient("Анна", 18)
    planner.add_recipient("Борис", 35)
    planner.add_recipient("Виктория", 28)

    # Добавляем поводы
    planner.add_occasion("День рождения", "День рождения", 1, 200, "подарочный сертификат")
    planner.add_occasion("Новый год", "Новый год", 1, 150, "подарочная коробка")
    planner.add_occasion("День святого Валентина", "День святого Валентина", 1, 100, "цветы")

    # Добавляем бюджет
    planner.add_budget("Общий бюджет", 2000)

    # Добавляем статусы покупки
    planner.add_purchase_status("Запланировано")
    planner.add_purchase_status("В процессе")
    planner.add_purchase_status("Готово")

    # Показываем данные
    print("=== Получатели ===")
    planner.print_recipients()

    print("\n=== Поводы ===")
    planner.print_occasions()

    print("\n=== Бюджет ===")
    planner.print_budgets()

    print("\n=== Статусы покупки ===")
    planner.print_purchase_statuses()

    # Добавляем подарок и показываем его
    gift = planner.add_gift("Анна", "День рождения", 300, "Подарочный сертификат в магазин косметики")
    print(f"\n=== Добавленный подарок ===")
    print(f"Получатель: {gift.recipient}")
    print(f"Повод: {gift.occasion}")
    print(f"Бюджет: {gift.budget}")
    print(f"Описание: {gift.description}")
    print(f"Статус: {gift.status}")

    # Показываем все подарки
    print("\n=== Все подарки ===")
    planner.print_gifts()

    # Показываем статистику
    print("\n=== Статистика ===")
    planner.print_statistics()

    # Показываем график
    print("\n=== График расходов ===")
    planner.print_spending_chart()

    # Показываем напоминания
    print("\n=== Напоминания ===")
    planner.print_reminders()

    print("\nДемонстрация завершена!")

if __name__ == "__main__":
    demo()
