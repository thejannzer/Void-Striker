import pygame
import time
import random

class Meteor:
    def __init__(self):
        self.meteor = pygame.image.load("images/meteor_squareDetailedSmall.png")
        self.x = 500-64
        self.y = 64

    def draw (self, screen):
        screen.blit(self.meteor, (self.x, self.y))