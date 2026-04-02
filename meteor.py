import pygame
import random

class Meteor:
    def __init__(self):
        self.image = pygame.image.load("images/meteor_squareDetailedSmall.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 1920 - 64)
        self.rect.y = -64
        self.speed = 10
        

    def update(self):
        self.rect.y += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        



        

