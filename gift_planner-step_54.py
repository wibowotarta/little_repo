# === Stage 54: Добавь режим избранных записей и быстрый доступ к ним ===
# Project: GiftPlanner
def show_favorites():
    """Показать избранные записи (быстрый доступ)."""
    favorites = [r for r in records if getattr(r, 'is_favorite', False)]
    if not favorites:
        print("\nНет избранных записей. Добавьте понравившиеся с помощью toggle_favorite().")
        return
    print(f"\n=== Избранные записи ({len(favorites)}) ===")
    for i, r in enumerate(favorites, 1):
        print(f"  {i}. {r}")
    print()
