# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: GiftPlanner
import sys

class UndoManager:
    def __init__(self):
        self.history = []
        self.max_depth = 10

    def record(self, action_name, state_snapshot):
        if len(self.history) >= self.max_depth:
            del self.history[0]
        self.history.append((action_name, state_snapshot))

    def can_undo(self):
        return len(self.history) > 0

    def undo_last(self):
        if not self.can_undo():
            print("Нечего откатывать.")
            return False
        action_name, snapshot = self.history.pop()
        print(f"Откат: действие '{action_name}'")
        return snapshot

def main():
    import os, json
    data_file = "gift_data.json"

    def load():
        if not os.path.exists(data_file):
            return {"receivers": [], "occasions": {}, "budgets": {}}, 0
        with open(data_file) as f:
            raw = json.load(f)
        receivers = raw.get("receivers", [])
        occasions = {k: v for k, v in raw["occasions"].items()}
        budgets = {k: v for k, v in raw["budgets"].items()}
        return {"receivers": receivers, "occasions": occasions, "budgets": budgets}, 0

    def save(data):
        with open(data_file, "w") as f:
            json.dump(data, f, indent=2)

    undo_mgr = UndoManager()
    current_data, _ = load()

    action_name = input("Название действия для отката (или 'q' чтобы выйти): ").strip().lower() or "q"
    if action_name == "q":
        sys.exit(0)

    snapshot = {
        "receivers_count": len(current_data["receivers"]),
        "occasions_count": len(current_data["occasions"]),
        "budgets_count": len(current_data["budgets"]),
    }
    undo_mgr.record(action_name, snapshot)

    print("Сделайте действие...")
    # Имитация: загружаем новое состояние (в реальном проекте — результат действия)
    new_state = input("Введите количество получателей после действия (или 'q' чтобы пропустить): ").strip() or "q"
    if new_state == "q":
        sys.exit(0)

    current_data["receivers"] = [{"name": f"Получатель_{i}", "occasion": "", "budget": 0, "status": "planned"} for i in range(int(new_state))]
    save(current_data)

    print("Действие выполнено.")
