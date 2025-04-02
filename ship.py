import pygame

class Ship:
    """Class tomanage the game ship"""

    def __init__(self, ai_game):
        """Initialize the ship and configurate its initial position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect
        self.image = pygame.image.load('images/ship (1).bmp')
        self.rect = self.image.get_rect()

        # Place initially the ship at the midbottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship horizontal position
        self.x = float(self.rect.x)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update ship position according to movement flags"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update the rect object of self.x
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current position"""
        self.screen.blit(self.image, self.rect)
