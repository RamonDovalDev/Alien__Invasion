import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Class to represent one alien on the fleet"""

    def __init__(self, ai_game):
        """Initialize the alien and establish its initial position"""
        super().__init__()
        self.screen = ai_game.screen

        # Load the alien image and configurate its rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # New alien at the left top of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien horizontal position
        self.x = float(self.rect.x)