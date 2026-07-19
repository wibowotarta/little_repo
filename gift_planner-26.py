# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: GiftPlanner
def run_demo():
    """Демо-команды для ручного тестирования GiftPlanner."""
    from gift_planner import GiftPlanner, Recipient, Occasion, Status
    
    planner = GiftPlanner()
    
    recipients = [
        Recipient("Мария", "День рождения"),
        Recipient("Иван", "Новый год"),
        Recipient("Анна", "Свадьба"),
    ]
    
    occasions = {
        "День рождения": Occasion(100),
        "Новый год": Occasion(300),
        "Свадьба": Occasion(200),
    }
    
    planner.add_recipients(recipients)
    planner.set_occasions(occasions)
    
    budget = 500
    
    while True:
        print("\n=== GiftPlanner Demo ===")
        print(f"Бюджет: {budget} руб.")
        
        for r in recipients:
            occasion = occasions.get(r.occasion, Occasion(100))
            if planner.can_buy_gift(r.name, budget):
                gift = planner.buy_gift(r.name)
                status_text = "✓ Покупка успешна!"
                budget -= gift.price
            else:
                status_text = "✗ Недостаточно средств."
            
            print(f"  {r.name}: {occasion.occasion} - {gift.description if hasattr(gift, 'description') else 'N/A'} ({status_text})")
        
        try:
            user_input = input("\nДействие (1-покупка, 2-бюджет, 3-выход): ")
        except EOFError:
            break
        
        if user_input == "1":
            continue
        elif user_input == "2":
            budget = int(input("Новый бюджет: "))
        elif user_input == "3":
            print(f"Итого потрачено: {500 - budget} руб.")
            break
