# === Stage 32: Добавь журнал действий пользователя ===
# Project: GiftPlanner
import json
from datetime import datetime, timezone

class ActionLog:
    def __init__(self):
        self.entries = []

    def log(self, action_type: str, target_id: int, detail: str) -> None:
        entry = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "action": action_type,
            "target_id": target_id,
            "detail": detail,
        }
        self.entries.append(entry)

    def get_log(self, max_entries=20) -> list:
        return self.entries[-max_entries:]

    def clear(self) -> None:
        self.entries.clear()
