import pygame

class Ship:
    def __init__(self):
        self.ship = pygame.image.load("images/ship_G.png")
        self.start_x = 960 - 64
        self.start_y = 540 - 64
        self.bullets = []

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
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            bullet = pygame.Rect(self.start_x + 27, self.start_y, 10, 10)
            self.bullets.append(bullet)
            
    def update_bullets(self, screen):
        for bullet in self.bullets:
            pygame.draw.rect(screen, (250, 250, 250), bullet)
            bullet.y -= 15
            if bullet.y < 0:
                self.bullets.remove(bullet)

