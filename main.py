import pygame
from ship import Ship
from meteor import Meteor

# pygame setup
pygame.init()
pygame.mixer.init()
music = pygame.mixer.music.load('sounds/retro-music.mp3')
crash = pygame.mixer.Sound('sounds/crash-sound.mp3')
screen = pygame.display.set_mode((1920, 1080))
background = pygame.image.load("images/background.jpg").convert()
pygame.display.set_caption("Void Striker")
clock = pygame.time.Clock()
running = True

bg_color = (10, 0, 50)

score = 0

ship = Ship()

meteors = []

game_over = False

won = False

spawn_rate = 1000
level = 1

#eigenes Event für Meteor-Spawn
SPAWN_METEOR = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_METEOR, spawn_rate)  # alle 1000 ms

def score_text(text):
    font = pygame.font.SysFont("arial", 40)
    text_surface = font.render(text, True, (255, 255, 255))
    screen.blit(text_surface, (20, 20))

def level_text(text):
    font = pygame.font.SysFont("arial", 40)
    text_surface = font.render(text, True, (255, 255, 255))
    screen.blit(text_surface, (1750, 20))
 
pygame.mixer.music.play(-1)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == SPAWN_METEOR:
            meteors.append(Meteor())

    screen.blit(background, (0, 0))

    for meteor in meteors:
        meteor.update()
        meteor.draw(screen)

    if not game_over and not won:
        ship.move()
        ship.shoot(screen)
        ship.update_bullets(screen)
        ship.draw(screen)

    elif game_over == True:
        pygame.mixer.music.stop()
        screen.fill((0,0,0))
        font = pygame.font.SysFont(None, 80)
        text = font.render("GAME OVER", True, (255, 0, 0))
        meteors.clear()
        screen.blit(text, (800, 400))

    elif won == True:
        pygame.mixer.music.stop()
        pygame.mixer.music.load('sounds/applause.mp3')
        pygame.mixer.music.play(-1)
        screen.fill((0, 100, 10))
        meteors.clear()
        font = pygame.font.SysFont(None, 80)
        text = font.render("YOU WON!", True, (0, 255, 0))
        screen.blit(text, (800, 400))


    #Kollision Bullet
    for bullet in ship.bullets[:]:           #[:] macht eine Kopie der Liste... verhindert Fehler beim entfernen
        for meteor in meteors[:]:
            if bullet.colliderect(meteor.rect):
                crash.play()
                ship.bullets.remove(bullet)
                meteors.remove(meteor)
                score += 1
                break
    
    #Kollision Ship
    if not game_over:
        for meteor in meteors[:]:
            if ship.rect.colliderect(meteor.rect):
                crash.play()
                game_over = True
                break

    #nächstes Level
    if score >= 3 and level == 1:
        level = 2
        pygame.time.set_timer(SPAWN_METEOR, 500)

    elif score >= 5 and level == 2:
        ship.shoot_delay = 220
        ship.bullet_color = (255, 0, 0)
        level = 3
        pygame.time.set_timer(SPAWN_METEOR, 250)

    elif score >= 10 and level == 3:
        pygame.mixer.music.stop()
        pygame.mixer.music.load('sounds/level4-music.mp3')
        pygame.mixer.music.play(-1)
        level = 4
        pygame.time.set_timer(SPAWN_METEOR, 150)

    elif score >= 15 and level == 4:
        ship.shoot_delay = 150
        ship.bullet_color = (60, 220, 210)
        level = 5
        pygame.time.set_timer(SPAWN_METEOR, 100)
    
    elif score >= 50:
        won = True

    score_text(f"Score: {score}")
    level_text(f"Level: {level}")

    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()