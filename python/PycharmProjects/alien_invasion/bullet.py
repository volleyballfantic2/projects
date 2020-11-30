import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A sprite class for the bullet"""

    def __init__(self, ai_game):
        """ Create a bullet fired from ship        """
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at 0,0 and then position it
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # store bullets vert position as decimal
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet op the screen"""
        # Update the bullets decimal position
        self.y -= self.settings.bullet_speed
        # update bullets y vert position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet oup the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
