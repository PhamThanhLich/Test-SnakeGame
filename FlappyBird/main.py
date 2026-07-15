import os
import pygame
from random import randint


pygame.init()
WEIGHT, HEIGHT = 400, 600
screen = pygame.display.set_mode((WEIGHT, HEIGHT))
pygame.display.set_caption("Flappy Bird")
running = True
GREEN = (0, 200, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
clock = pygame.time.Clock()

TUBE_WIDTH = 50
TUBE_VELOCITY = 3
YUBE_GAP = 150
BIRD_X = 50
BIRD_WIDTH = 35
BIRD_HEIGHT = 35
GRAVITY = 0.5
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

score = 0
font = pygame.font.SysFont('sans', 20)
bird_drop_velocity = 0
bird_y = 400
tube1_x = 600
tube1_height = randint(100, 400)
tube2_x = 800
tube2_height = randint(100, 400)
tube3_x = 1000
tube3_height = randint(100, 400)
tube1_passed = False
tube2_passed = False
tube3_passed = False

pause = False
background_image = pygame.image.load("FlappyBird/background.png")
bird_image = pygame.image.load("FlappyBird/bird.png")

while running:
    clock.tick(60)
    screen.fill(GREEN)
    screen.blit(background_image, (-50, -50))

    # Ve ong tren         
    tube1_rect =  pygame.draw.rect(screen, BLUE, (tube1_x, 0, TUBE_WIDTH, tube1_height))
    tube2_rect = pygame.draw.rect(screen, BLUE, (tube2_x, 0, TUBE_WIDTH, tube2_height))
    tube3_rect = pygame.draw.rect(screen, BLUE, (tube3_x, 0, TUBE_WIDTH, tube3_height))

    # Ve ong duoi
    tube1_inv = pygame.draw.rect(screen,BLUE,(tube1_x, tube1_height + YUBE_GAP, TUBE_WIDTH, HEIGHT - tube1_height - YUBE_GAP))
    tube2_inv = pygame.draw.rect(screen,BLUE,(tube2_x, tube2_height + YUBE_GAP, TUBE_WIDTH, HEIGHT - tube2_height - YUBE_GAP))
    tube3_inv = pygame.draw.rect(screen,BLUE,(tube3_x, tube3_height + YUBE_GAP, TUBE_WIDTH, HEIGHT - tube3_height - YUBE_GAP))

    tube1_x = tube1_x - TUBE_VELOCITY
    tube2_x = tube2_x - TUBE_VELOCITY
    tube3_x = tube3_x - TUBE_VELOCITY

    sant_rect = pygame.draw.rect(screen, YELLOW, (0, 550, WEIGHT, 50))

    # tao chim
    bird_rect = screen.blit(bird_image, (BIRD_X, bird_y))
    bird_y += bird_drop_velocity
    bird_drop_velocity += GRAVITY

    # Tao lai ong
    if tube1_x < -TUBE_WIDTH:
        tube1_x = 550
        tube1_height = randint(100, 400)
        tube1_passed = False
    if tube2_x < -TUBE_WIDTH:
        tube2_x = 550
        tube2_height = randint(100, 400)
        tube2_passed = False
    if tube3_x < -TUBE_WIDTH:
        tube3_x = 550
        tube3_height = randint(100, 400)
        tube3_passed = False

    # Hien thi diem
    Score_txt = font.render("Score: " + str(score), True, BLACK)
    screen.blit(Score_txt, (5, 5))
    # Cong diem
    if tube1_x + TUBE_WIDTH <= BIRD_X and tube1_passed == False:
        score += 1
        tube1_passed = True
    if tube2_x + TUBE_WIDTH <= BIRD_X and tube2_passed == False:
        score += 1
        tube2_passed = True
    if tube3_x + TUBE_WIDTH <= BIRD_X and tube3_passed == False:
        score += 1
        tube3_passed = True

    # Kiem tra va cham
    for tube in [tube1_rect,tube2_rect,tube3_rect,tube1_inv,tube2_inv,tube3_inv, sant_rect]:
        if bird_rect.colliderect(tube):
            TUBE_VELOCITY = 0
            bird_drop_velocity = 0
            pause = True
            game_over_txt = font.render('Game Over, Score: ' + str(score), True, BLACK)
            screen.blit(game_over_txt, (100, 300))
            press_space_txt = font.render('Press Space to Restart', True, BLACK)
            screen.blit(press_space_txt, (100, 350))

    for event in pygame.event.get():    
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_drop_velocity = 0
                bird_drop_velocity -= 10
                if pause == True:
                    pause = False
                    TUBE_VELOCITY = 3
                    bird_y = 400
                    tube1_x = 600
                    tube1_height = randint(100, 400)
                    tube2_x = 800
                    tube2_height = randint(100, 400)
                    tube3_x = 1000
                    tube3_height = randint(100, 400)
                    score = 0

    pygame.display.flip()

pygame.quit()