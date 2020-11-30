class Settings:
    """Stores game settings"""

    def __init__(self):
        """Initialize the game settings"""
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (63, 72, 204)

        # Ship settings
        self.ships_speed = 1.5
        self.ship_limit = 3

        # bullet settings
        self.bullet_speed = 3.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien Ship
        self.alien_speed = 1.0
        self.fleet_drop_speed = 15
        # direction 1 = right, -1 = left
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50
        self.score_scale = 1.5

        # Game speeds
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ships_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        self.fleet_direction = 1

    def increase_speed(self):
        self.ships_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)

