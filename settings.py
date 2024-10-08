import pygame

class Settings():
    def __init__(self):
        pygame.init()

        display_info = pygame.display.Info()
        
        self.screen_width = display_info.current_w
        self.screen_height = display_info.current_h
        
        self.bg_color = (0, 0, 50)
        
        self.ship_speed = 1.0
        self.ship_limit = 3
        self.ship_vertical_offset = 15

        self.alien_speed = 0.7
        self.alien_points = 50
        self.fleet_drop_speed = 10

        self.bullet_speed = 1
        self.bullet_width = 2
        self.bullet_height = 15
        self.bullet_color = (250, 250, 250)
        self.bullets_allowed = 5

        self.speedup_scale = 1.1

        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3.0
        self.alien_speed_factor = 1.0

        self.fleet_direction = 1

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)