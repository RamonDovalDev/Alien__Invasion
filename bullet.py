import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Class to manage the bullets shot by the ship"""

    def __init__(self, ai_game):
        """Make a bullet object at ship current position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Make a rect for the bullet at (0, 0) and then establish its right position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store a decimal value for bullet position
        self.y = float(self.rect.y)

    def update(self):
        """Move the buller up the screen"""
        # Update the bullet decimal value
        self.y -= self.settings.bullet_speed
        # Update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw a bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)

