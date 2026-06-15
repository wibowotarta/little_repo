# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: GiftPlanner
def delete_gift(gift_id: int) -> bool:
    if gift_id not in gifts:
        print(f"Ошибка: Подарок с ID {gift_id} не найден.")
        return False
    
    del gifts[gift_id]
    print(f"Подарок с ID {gift_id} успешно удален.")
    return True

def delete_recipient(recipient_id: int) -> bool:
    if recipient_id not in recipients:
        print(f"Ошибка: Получатель с ID {recipient_id} не найден.")
        return False
    
    for gift_list in gifts.values():
        for i, gift_data in enumerate(gift_list):
            if gift_data.get('recipient_id') == recipient_id:
                del gift_list[i]
                break
    
    del recipients[recipient_id]
    print(f"Получатель с ID {recipient_id} успешно удален.")
    return True

def delete_occasion(occasion_id: int) -> bool:
    if occasion_id not in occasions:
        print(f"Ошибка: Повод с ID {occasion_id} не найден.")
        return False
    
    del occasions[occasion_id]
    print(f"Повод с ID {occasion_id} успешно удален.")
    return True

def delete_budget(budget_id: int) -> bool:
    if budget_id not in budgets:
        print(f"Ошибка: Бюджет с ID {budget_id} не найден.")
        return False
    
    del budgets[budget_id]
    print(f"Бюджет с ID {budget_id} успешно удален.")
    return True
