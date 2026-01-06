import pygame
from ship import Ship

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Void Striker")
clock = pygame.time.Clock()
running = True

ship = Ship()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((10, 0, 50))

    # RENDER YOUR GAME HERE
    ship.move()
    ship.shoot(screen)
    ship.update_bullets(screen)
    ship.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()