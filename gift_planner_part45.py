# === Stage 45: Добавь восстановление из резервной копии ===
# Project: GiftPlanner
import shutil, os

def restore_backup():
    backup_path = "gift_planner_backup.py"
    if not os.path.exists(backup_path):
        return "Резервная копия не найдена."
    shutil.copy2(backup_path, "gift_planner.py")
    return "Резервная копия успешно восстановлена."
