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
        self.high_score = 0

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.drop_counter = 0
        self.score = 0
