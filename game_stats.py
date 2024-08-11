import json

class GameStats:
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False

        # Завантаження рекорду з файлу
        self.high_score = self._load_high_score()

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def _load_high_score(self):
        """Завантажує рекорд з файлу, якщо він існує."""
        try:
            with open('high_score.json', 'r') as f:
                return int(json.load(f))
        except FileNotFoundError:
            return 0

    def save_high_score(self):
        """Зберігає рекорд у файл."""
        with open('high_score.json', 'w') as f:
            json.dump(self.high_score, f)
