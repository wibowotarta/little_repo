# === Stage 29: Добавь конфигурацию приложения через словарь настроек ===
# Project: GiftPlanner
APP_CONFIG = {
    "app_name": "GiftPlanner",
    "version": "0.29",
    "currency_symbol": "$",
    "default_budget": 100,
    "max_recipients": 50,
    "statuses": ["planned", "ordered", "shipped", "received"],
    "allowed_events": [
        "birthday", "anniversary", "christmas", "new_year", "graduation"
    ],
}


def get_config(key: str) -> Any:
    """Return a config value, raise KeyError if missing."""
    return APP_CONFIG[key]


def set_config(key: str, value: Any) -> None:
    """Update or add a config entry."""
    APP_CONFIG[key] = value


def reset_config() -> dict:
    """Reset to default configuration and return it."""
    global APP_CONFIG
    APP_CONFIG = {
        "app_name": "GiftPlanner",
        "version": "0.29",
        "currency_symbol": "$",
        "default_budget": 100,
        "max_recipients": 50,
        "statuses": ["planned", "ordered", "shipped", "received"],
        "allowed_events": [
            "birthday", "anniversary", "christmas", "new_year", "graduation"
        ],
    }
    return dict(APP_CONFIG)
