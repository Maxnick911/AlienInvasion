import pygame

class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load('images\\ship.png')
        self.rect = self.image.get_rect()

        # Встановлюємо початкову позицію корабля
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        # Оновлюємо позицію корабля в залежності від напрямку руху
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Оновлюємо rect з плаваючої координати x
        self.rect.x = self.x

    def blitme(self):
        # Відображення корабля на екрані
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        # Використовуємо параметр з налаштувань для відступу
        offset = self.settings.ship_vertical_offset
        self.rect.midbottom = (self.screen_rect.midbottom[0], self.screen_rect.bottom - offset)
        self.x = float(self.rect.x)

