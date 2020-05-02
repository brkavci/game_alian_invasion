class GameStats:
    """Track statistics for Alien Invasion."""

    # High_score = 500

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.drop_counter = 0
        self.reset_stats()
        self.game_active = False

        # High score should never be reset.
        self.hs_file = "highscore.txt"
        self.high_score = self._get_highscore(self.hs_file)

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.drop_counter = 0
        self.score = 0
        self.level = 1

    def _get_highscore(self, file_name):
        """Reads all time highscore from the txt file"""
        try:
            with open(f'{file_name}') as hs:
                high_score = int(hs.read())
        except (FileNotFoundError, ValueError):
            return 0
        else:
            return high_score

    def save_highscore(self, file_name):
        """Writes high score to the txt file if there is new"""
        current_hs = self._get_highscore(self.hs_file)
        if self.high_score > current_hs:
            with open(f'{file_name}', mode='w') as hs:
                hs.write(str(self.high_score))
