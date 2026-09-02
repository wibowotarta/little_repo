# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: GiftPlanner
class Color:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'
    HIDDEN = '\033[8m'
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    GRAY = '\033[90m'
    LIGHT_GRAY = '\033[37m'
    DARK_RED = '\033[91m'
    DARK_GREEN = '\033[92m'
    DARK_YELLOW = '\033[93m'
    DARK_BLUE = '\033[94m'
    DARK_MAGENTA = '\033[95m'
    DARK_CYAN = '\033[96m'
    DARK_WHITE = '\033[97m'

class Colors:
    def __init__(self, enabled):
        self._enabled = enabled

    @property
    def enabled(self):
        return self._enabled

    def __getattr__(self, name):
        if not self._enabled:
            return self.RESET
        return getattr(Color, name, self.RESET)

    def __call__(self, text):
        if not self._enabled:
            return text
        return text

    def __str__(self):
        return '' if not self._enabled else ''
