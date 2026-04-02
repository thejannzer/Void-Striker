import pygame
from ship import Ship
from meteor import Meteor

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Void Striker")
clock = pygame.time.Clock()
running = True

score = 0

ship = Ship()

meteors = []

#eigenes Event für Meteor-Spawn
SPAWN_METEOR = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_METEOR, 1000)  # alle 1000 ms

def score_text(text):
    font = pygame.font.SysFont("arial", 40)
    text_surface = font.render(text, True, (255, 255, 255))
    screen.blit(text_surface, (20, 20))
 

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
        meteor.update()
        meteor.draw(screen)

    #Kollision
    for bullet in ship.bullets[:]:           #[:] macht eine Kopie der Liste... verhindert Fehler beim entfernen
        for meteor in meteors[:]:
            if bullet.colliderect(meteor.rect):
                ship.bullets.remove(bullet)
                meteors.remove(meteor)
                score += 1
                break
    
    score_text(f"Score: {score}")

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()