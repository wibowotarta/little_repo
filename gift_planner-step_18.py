# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: GiftPlanner
class TagManager:
    def __init__(self, db):
        self.db = db
        self._tags_cache = {}

    def add_tag(self, name: str) -> None:
        if not self._tags_cache.get(name):
            self.db.execute("INSERT INTO tags (name) VALUES (?)", (name,))
            self._tags_cache[name] = True

    def remove_tag(self, tag_name: str) -> int:
        rows_deleted = self.db.execute(
            "DELETE FROM gift_recipient_tags WHERE tag_name = ?",
            (tag_name,)
        )
        if rows_deleted > 0 and tag_name in self._tags_cache:
            del self._tags_cache[tag_name]
        return rows_deleted

    def get_tagged_gifts(self, tag_name: str) -> list[dict]:
        cursor = self.db.execute(
            "SELECT gr.id, gr.name as recipient, g.title as gift_title FROM gifts g JOIN gift_recipients gr ON g.id = gr.gift_id LEFT JOIN gift_recipient_tags grt ON gr.id = grt.recipient_id WHERE grt.tag_name = ?",
            (tag_name,)
        )
        return cursor.fetchall()

    def sync_tags_from_db(self) -> None:
        cursor = self.db.execute("SELECT DISTINCT tag_name FROM gift_recipient_tags")
        for row in cursor:
            self._tags_cache[row[0]] = True
