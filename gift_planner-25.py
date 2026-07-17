# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: GiftPlanner
def parse_date(raw):
    """Парсит дату в формате ДД.ММ.ГГГГ, возвращает datetime.date или строку-описание ошибки."""
    if not isinstance(raw, str) or not raw.strip():
        return "Ошибка: дата не может быть пустой."
    parts = raw.split(".")
    if len(parts) != 3:
        return "Ошибка: неверный формат даты. Используйте ДД.ММ.ГГГГ."
    day, month, year = int(parts[0].strip()), int(parts[1].strip()), int(parts[2].strip())
    try:
        return date(year, month, day)
    except ValueError as e:
        if "month" in str(e):
            return f"Ошибка: {month} — не существует. Проверьте месяц."
        elif "day" in str(e):
            return f"Ошибка: {day} — выход за пределы месяца. Проверьте число."
        else:
            return "Ошибка: неизвестная ошибка при парсинге даты."
