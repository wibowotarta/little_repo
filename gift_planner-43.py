# === Stage 43: Добавь пагинацию длинных списков ===
# Project: GiftPlanner
def paginate(items, page_size=10):
    total_pages = (len(items) + page_size - 1) // page_size
    page = 1
    while True:
        start = (page - 1) * page_size
        end = start + page_size
        page_items = items[start:end]
        print(f"\n--- Страница {page}/{total_pages} ---")
        for item in page_items:
            print(item)
        if start >= len(items):
            break
        page += 1
