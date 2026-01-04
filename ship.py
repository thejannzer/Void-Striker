import pygame

class Ship:
    def __init__(self):
        self.ship = pygame.image.load("images/ship_G.png")
        self.start_x = 960 - 64
        self.start_y = 540 - 64

    def draw(self, screen):
        screen.blit(self.ship, (self.start_x, self.start_y))

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.start_x -= 8
        if keys[pygame.K_RIGHT]:
            self.start_x += 8
        if keys[pygame.K_UP]:
            self.start_y -= 8
        if keys[pygame.K_DOWN]:
            self.start_y += 8

    def shoot(self, screen):
        pr = pygame.Rect(self.start_x + 64, self.start_y, 10, 10)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            pygame.draw.rect(screen, (0, 0, 0), pr)
            # wie Rechteck nach oben bewegen?

