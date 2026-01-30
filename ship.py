import pygame
import time

class Ship:
    pygame.mixer.init()
    def __init__(self):
        self.ship = pygame.image.load("images/ship_G.png")
        self.start_x = 960 - 64
        self.start_y = 540 - 64
        self.bullets = []
        self.shoot_delay = 300
        self.last_shoot = 0
        #self.sound = pygame.mixer.Sound('''pfad zur datei''')

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
        current_time = pygame.time.get_ticks()
        if keys[pygame.K_SPACE]:
            if current_time - self.last_shoot >= self.shoot_delay:
                bullet = pygame.Rect(self.start_x + 27, self.start_y, 10, 10)
                #Shoot Sound einfügen (sound.play())
                self.bullets.append(bullet)
                self.last_shoot = current_time
            
    def update_bullets(self, screen):
        for bullet in self.bullets:
            pygame.draw.rect(screen, (250, 250, 250), bullet)
            bullet.y -= 15
            if bullet.y < 0:
                self.bullets.remove(bullet)

