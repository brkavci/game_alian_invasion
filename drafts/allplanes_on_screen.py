import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.__init__("Alien Invasion")
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion by brkavci")

        self.ship = Ship(self)

        self.ship2 = Ship(self)
        self.ship2.image = pygame.image.load('images/ships/black_hawk.bmp')
        self.ship2.rect.topleft = self.ship.rect.topright
        self.ship2.rect.centerx += 20

        self.ship3 = Ship(self)
        self.ship3.image = pygame.image.load('images/ships/blue_rocket.bmp')
        self.ship3.rect.topleft = self.ship2.rect.topright
        self.ship3.rect.centerx += 20

        self.ship4 = Ship(self)
        self.ship4.image = pygame.image.load('images/ships/ghost.bmp')
        self.ship4.rect.topleft = self.ship3.rect.topright
        self.ship4.rect.centerx += 20

        self.ship5 = Ship(self)
        self.ship5.image = pygame.image.load('images/ships/military.bmp')
        self.ship5.rect.topleft = self.ship4.rect.topright
        self.ship5.rect.centerx += 20

        self.ship6 = Ship(self)
        self.ship6.image = pygame.image.load('images/ships/russian.bmp')
        self.ship6.rect.topleft = self.ship5.rect.topright
        self.ship6.rect.centerx += 30

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            self.ship2.blitme()
            self.ship3.blitme()
            self.ship4.blitme()
            self.ship5.blitme()
            self.ship6.blitme()

            print(f'type1:{type(self.ship.rect)}')
            print(type(self.ship2.rect))

            # Make the most recently drawn screen visible.
            pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
