import pygame
import sys
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    """Class to mange game resources and behavior"""

    def __init__(self):
        """Initialize the game and make resources"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption('Alien Nation')

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Main loop for the game"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()

    def _check_events(self):
        """Key pressing and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _check_keydown_events(self, event):
        """Key pressing events"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event == pygame. K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Key releasing"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event == pygame. K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Make a new bullet and add it to the bullets group"""
        if (len(self.bullets)) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update the bullets position and get rid off the old ones"""
        self.bullets.update()
        # Get rid off the shot bullets
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_screen(self):
        """Update screen images and change to new screen"""    
        # Redraw the screen at each step of the loop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # Make visible the last drawn page
        pygame.display.flip()

if __name__ == '__main__':
    # Make an instance of the game and execute it
    ai = AlienInvasion()
    ai.run_game()