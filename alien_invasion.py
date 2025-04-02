import pygame
import sys
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Class to mange game resources and behavior"""

    def __init__(self):
        """Initialize the game and make resources"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption('Alien Nation')

        self.ship = Ship(self)

    def run_game(self):
        """Main loop for the game"""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """Key pressing and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()    

    def _update_screen(self):
        """Update screen images and change to new screen"""    
        # Redraw the screen at each step of the loop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # Make visible the last drawn page
        pygame.display.flip()

if __name__ == '__main__':
    # Make an instance of the game and execute it
    ai = AlienInvasion()
    ai.run_game()