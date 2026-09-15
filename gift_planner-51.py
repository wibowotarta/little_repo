# === Stage 51: Добавь журнал изменений данных с отметками времени ===
# Project: GiftPlanner
import json
from datetime import datetime

CHANGES_LOG = []

def log_change(action, data_summary):
    CHANGES_LOG.append({
        "timestamp": datetime.now().isoformat(),
        "action": action,
        "summary": data_summary
    })

def get_changes_log():
    return CHANGES_LOG

def clear_changes_log():
    CHANGES_LOG.clear()
