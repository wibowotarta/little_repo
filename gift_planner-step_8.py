# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: GiftPlanner
def run_cli():
    while True:
        print("\n=== GiftPlanner CLI ===")
        print("1. Показать всех получателей")
        print("2. Добавить нового получателя")
        print("3. Создать повод для подарка")
        print("4. Установить статус покупки")
        print("5. Выйти")
        choice = input("Выберите действие: ").strip()

        if choice == "1":
            for rec in recipients.values():
                print(f"\nИмя: {rec['name']}, Подарки: {', '.join(rec.get('gifts', []))}")
        elif choice == "2":
            name = input("Имя получателя: ")
            if not name or name in recipients:
                print("Ошибка имени")
            else:
                recipients[name] = {"name": name, "gifts": [], "budget": 0}
                print(f"Получатель '{name}' добавлен.")
        elif choice == "3":
            if not recipients:
                print("Нет получателей для подарка")
                continue
            rec_name = input("Имя получателя: ")
            reason = input("Повод (свадьба, день рождения): ")
            budget_str = input("Бюджет: ")
            try:
                budget = float(budget_str) if budget_str else 0.0
            except ValueError:
                print("Неверный формат бюджета")
                continue

            gift_id = len(recipients[rec_name]['gifts']) + 1
            recipients[rec_name]['gifts'].append({
                "id": gift_id,
                "reason": reason,
                "budget": budget,
                "status": "planned"
            })
            print(f"Подарок #{gift_id} добавлен.")
        elif choice == "4":
            if not recipients:
                print("Нет получателей")
                continue
            rec_name = input("Имя получателя: ")
            gift_idx_str = input("Номер подарка (или 'all' для всех): ").strip()
            try:
                gift_idx = int(gift_idx_str) - 1 if gift_idx_str.isdigit() else None
            except ValueError:
                print("Неверный номер подарка")
                continue

            status = input("Новый статус (planned, bought, shipped): ")
            for rec_name_key, rec_data in recipients.items():
                if rec_name == rec_name_key:
                    gifts_to_update = [rec_data['gifts'][i] for i in range(len(rec_data['gifts']))] if gift_idx is None else [rec_data['gifts'][gift_idx]]
                    for g in gifts_to_update:
                        old_status = g["status"]
                        g["status"] = status
                        print(f"Подарок #{g['id']} ({old_status} -> {status}) обновлен.")

        elif choice == "5":
            break
        else:
            print("Неверный выбор")
