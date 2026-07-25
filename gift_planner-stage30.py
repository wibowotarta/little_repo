# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: GiftPlanner
class Profile:
    def __init__(self, name, budget=100):
        self.name = name
        self.budget = budget

    def add_gift(self, gift_name, price, reason=""):
        if price > self.budget:
            return False
        self.budget -= price
        return True

    def get_status(self):
        return {"name": self.name, "remaining_budget": self.budget}


def main():
    profiles = [
        Profile("Alice", 200),
        Profile("Bob", 150),
        Profile("Charlie", 300),
    ]

    for profile in profiles:
        success = profile.add_gift("Gift for Mom", 80, "Birthday")
        print(f"{profile.name}: {'Added' if success else 'Skipped'} (budget: {profile.get_status()['remaining_budget']})")


main()
