# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: GiftPlanner
class GiftPlanner:
    def __init__(self):
        self._receivers = {}
        self._occasions = []
        self._budgets = {}
        self._purchases = {}

    def add_receiver(self, name: str) -> None:
        if not name.strip(): return
        self._receivers[name] = {"name": name.strip(), "notes": ""}

    def add_occasion(self, occasion: str, date: str | None = None) -> None:
        if not occasion.strip(): return
        self._occasions.append({"occasion": occasion.strip(), "date": date})

    def set_budget(self, receiver_name: str, amount: float) -> None:
        if receiver_name in self._receivers and amount >= 0:
            self._budgets[receiver_name] = round(amount, 2)

    def mark_purchased(self, occasion: str) -> bool:
        for item in self._occasions:
            if item["occasion"].lower() == occasion.lower():
                item["status"] = "purchased"
                return True
        return False
