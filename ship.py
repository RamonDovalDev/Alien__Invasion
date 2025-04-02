import pygame

class Ship:
    """Class tomanage the game ship"""

    def __init__(self, ai_game):
        """Initialize the ship and configurate its initial position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect
        self.image = pygame.image.load('images/ship (1).bmp')
        self.rect = self.image.get_rect()

        # Place initially the ship at the midbottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw the ship at its current position"""
        self.screen.blit(self.image, self.rect)
