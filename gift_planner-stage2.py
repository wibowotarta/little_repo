# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: GiftPlanner
class GiftPlanner:
    def __init__(self):
        self.recipients = {}
        self.reasons = ["День рождения", "Новый год", "Выходной", "Свадьба"]
        self.budgets = {"low": 1000, "medium": 5000, "high": 20000}

    def add_recipient(self, name, budget_level):
        if not name.strip():
            return False, "Имя получателя не может быть пустым."
        if budget_level not in self.budgets:
            return False, f"Неизвестный уровень бюджета. Доступные: {', '.join(self.budgets.keys())}."
        self.recipients[name] = {"budget": self.budgets[budget_level], "status": "planned"}
        return True, f"Получатель '{name}' добавлен с бюджетом {self.budgets[budget_level]}."

    def add_gift(self, recipient_name, reason):
        if recipient_name not in self.recipients:
            return False, f"Получатель '{recipient_name}' не найден."
        if reason not in self.reasons:
            return False, f"Неизвестный повод. Доступные: {', '.join(self.reasons)}."
        self.recipients[recipient_name]["reason"] = reason
        return True, f"Подарок для '{recipient_name}' по поводу '{reason}' добавлен."

    def get_summary(self):
        summary = []
        for name, data in self.recipients.items():
            summary.append(f"{name}: {data['reason']} (бюджет: {data['budget']}, статус: {data['status']})")
        return "\n".join(summary) if summary else "Список подарков пуст."
