# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: GiftPlanner
def suggest_next_actions(current_state):
    """Generate recommendations based on current planner state."""
    suggestions = []
    
    if not current_state.get("recipients", []):
        suggestions.append("Add recipients to start planning gifts.")
    
    reasons_without_recipients = [r for r in current_state["reasons"] 
                                   if not any(r["name"].lower() == rec["name"].lower() 
                                             for rec in current_state["recipients"])]
    if reasons_without_recipients:
        suggestions.append(f"Assign recipients to reason(s): {', '.join(r['name'] for r in reasons_without_recipients)}")
    
    planned_gifts = [g for g in current_state.get("gifts", []) if g.get("status")]
    unplanned_reasons = [r["id"] for r in current_state["reasons"] 
                         if not any(g["reason_id"] == r["id"] and g.get("status") for g in current_state.get("gifts", []))]
    if unplanned_reasons:
        suggestions.append(f"Plan gifts for reason(s): {', '.join(r['name'] for r in current_state['reasons'] if r['id'] in unplanned_reasons)}")
    
    budget_status = sum(g.get("budget_used", 0) for g in state.get("gifts", []))
    total_budget = state.get("total_budget", 1000)
    remaining = total_budget - budget_status
    if remaining <= 0 and planned_gifts:
        suggestions.append("Budget fully utilized. Consider adjusting budgets or adding more funds.")
    elif remaining < total_budget * 0.3 and planned_gifts:
        suggestions.append(f"Only {remaining:.1f}₽ remaining. Be selective with upcoming gifts.")
    
    if not current_state.get("history", []):
        suggestions.append("Consider setting up a history log to track past purchases.")
    
    if not current_state.get("notifications_enabled", False):
        suggestions.append("Enable notifications to stay updated on gift deadlines and budget alerts.")
    
    return suggestions[:3]  # Return top 3 suggestions max
