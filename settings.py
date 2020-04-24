class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1920
        self.screen_height = 1080
        self.screen_mode = 'F'  # 'F' Fullscreen,'W' Window mode
        self.bg_color = (158, 220, 233)

        # Ship settings
        self.ship_speed = 10
        self.ship_type = 'blue_rocket'
