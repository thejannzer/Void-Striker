import pygame
from ship import Ship
from meteor import Meteor

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Void Striker")
clock = pygame.time.Clock()
running = True

ship = Ship()

meteors = []

#eigenes Event für Meteor-Spawn
SPAWN_METEOR = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_METEOR, 1000)  # alle 1000 ms

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == SPAWN_METEOR:
            meteors.append(Meteor())

    screen.fill((10, 0, 50))

    # RENDER YOUR GAME HERE
    ship.move()
    ship.shoot(screen)
    ship.update_bullets(screen)
    ship.draw(screen)
    
    for meteor in meteors:
        meteor.draw(screen)
        meteor.update()

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()