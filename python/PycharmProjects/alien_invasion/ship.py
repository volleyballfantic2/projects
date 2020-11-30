import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """Manage the ship"""

    def __init__(self, ai_game):
        """Initialize the ship and set start position"""
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship and set starting position
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.x = 0.0
        # start each new ship at bottom middle of screen
        self.center_ship()

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ships position by movement flag
           and Limit movement to screen edges"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ships_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ships_speed

        # set the int rect position to self.x decimal
        self.rect.x = self.x

    def blit(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
