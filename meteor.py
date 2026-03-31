import pygame
import time
import random

class Meteor:
    def __init__(self):
        self.image = pygame.image.load("images/meteor_squareDetailedSmall.png")
        self.x = random.randint(0, 1920 - 64)
        self.y = -64
        self.speed = 10

    def update(self):
        self.y += self.speed

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        



        

