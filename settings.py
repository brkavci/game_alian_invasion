class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 1920
        self.screen_height = 1080
        self.screen_mode = 'W'  # 'F' Fullscreen,'W' Window mode
        self.bg_color = (158, 220, 233)

        # Ship settings
        self.ship_type = 'black_hawk'
        self.ship_limit = 2

        # Bullet settings
        self.bullet_height = 15
        self.bullet_color = (1, 1, 1)
        self.bullets_allowed = 7

        # Alien settings
        self.fleet_drop_speed = 15

        # How quickly the game speeds up
        self.ship_speedup_scale = 1.3
        self.alien_speedup_scale = 1.2

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 1.0
        self.bullet_speed = 1.0
        self.alien_speed = 0.3
        self.bullet_width = 3

        # Scoring
        self.alien_points = 200

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.ship_speedup_scale
        self.bullet_speed *= self.ship_speedup_scale
        self.bullet_width *= self.ship_speedup_scale
        self.alien_speed *= self.alien_speedup_scale
        self.alien_points *= 2
