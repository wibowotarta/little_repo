# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: GiftPlanner
import json

class UserProfile:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class ProfileManager:
    def __init__(self, storage_path="profiles.json"):
        self.profiles = {}
        self.active_profile_name = None
        self.storage_path = storage_path
        self._load_profiles()

    def _load_profiles(self):
        try:
            with open(self.storage_path, 'r') as f:
                data = json.load(f)
                for name, info in data.items():
                    self.profiles[name] = UserProfile(info['name'], info.get('email', ''))
                if 'active' in data and data['active']:
                    self.active_profile_name = data['active']
        except FileNotFoundError:
            pass

    def add_profile(self, name, email):
        self.profiles[name] = UserProfile(name, email)
        return name

    def switch_to(self, profile_name):
        if profile_name not in self.profiles:
            raise ValueError(f"Профиль '{profile_name}' не найден")
        self.active_profile_name = profile_name
        return True

    def save_profiles(self):
        data = {name: {'name': p.name, 'email': p.email} for name, p in self.profiles.items()}
        if self.active_profile_name:
            data['active'] = self.active_profile_name
        with open(self.storage_path, 'w') as f:
            json.dump(data, f, indent=2)

    def get_active_profile(self):
        if not self.active_profile_name:
            return None
        return self.profiles[self.active_profile_name]
