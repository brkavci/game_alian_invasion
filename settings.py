class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1920
        self.screen_height = 1080
        self.screen_mode = 'W'  # 'F' Fullscreen,'W' Window mode
        self.bg_color = (158, 220, 233)

        # Ship settings
        self.ship_type = 'black_hawk'
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (1, 1, 1)
        self.bullets_allowed = 7

        # Alien settings
        self.alien_speed = 0.5
        self.fleet_drop_speed = 15
        self.fleet_direction = 1  # 1 represents right -1 left
