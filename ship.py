import pygame

class Ship:
    def __init__(self):
        self.ship = pygame.image.load("images/ship_G.png")
        self.rect = self.ship.get_rect()
        self.start_x = 960 - 64
        self.start_y = 540 - 64
        self.rect.topleft = (self.start_x, self.start_y)
        self.bullets = []
        self.shoot_delay = 300
        self.last_shoot = 0
        self.sound = pygame.mixer.Sound('sounds/shoot.mp3')

    def draw(self, screen):
        screen.blit(self.ship, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.start_x -= 10
        if keys[pygame.K_RIGHT]:
            self.start_x += 10
        if keys[pygame.K_UP]:
            self.start_y -= 10
        if keys[pygame.K_DOWN]:
            self.start_y += 10
        
        self.rect.topleft = (self.start_x, self.start_y)

    def shoot(self, screen):
        keys = pygame.key.get_pressed()
        current_time = pygame.time.get_ticks()
        if keys[pygame.K_SPACE]:
            if current_time - self.last_shoot >= self.shoot_delay:
                self.sound.play()
                bullet = pygame.Rect(self.start_x + 27, self.start_y, 10, 10)
                self.bullets.append(bullet)
                self.last_shoot = current_time
            
    def update_bullets(self, screen):
        for bullet in self.bullets[:]:
            pygame.draw.rect(screen, (250, 250, 250), bullet)
            bullet.y -= 15
            if bullet.y < 0:
                self.bullets.remove(bullet)

