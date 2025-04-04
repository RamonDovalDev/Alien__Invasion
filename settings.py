class Settings:
    """Class to store all game configuration"""

    def __init__(self):
        # Screen configuration
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.bullets_allowed = 3

        # Ship configuration
        self.ship_speed = 1.5

        # Bullets configuration
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

        # Alien configuration
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction = 1 represents right; -1 represents left
        self.fleet_direction = 1