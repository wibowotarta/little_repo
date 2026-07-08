# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: GiftPlanner
def add_reminders():
    reminders = []
    while True:
        name = input("Имя получателя (или Enter для завершения): ").strip()
        if not name:
            break
        gift = input(f"Подарок для {name}: ").strip()
        date_str = input("Дата напоминания (ДД.ММ): ").strip()
        try:
            day, month = map(int, date_str.split('.'))
            if 1 <= day <= 31 and 1 <= month <= 12:
                reminders.append({"имя": name, "подарок": gift, "дата": f"{day}.{month}"})
            else:
                print("Неверный формат даты. Попробуйте ещё раз.")
        except ValueError:
            print("Ошибка ввода даты. Используйте формат ДД.ММ")

    return reminders
