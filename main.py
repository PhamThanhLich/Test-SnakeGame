import pygame
from time import sleep
from random import randint

pygame.init()
screen = pygame.display.set_mode((601, 601))
pygame.display.set_caption("Snake Game")
running = True
GREEN = (0, 200, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
clock = pygame.time.Clock()

snakes = [[5,6], [5,7]]
direction = "right"
apple = [randint(0, 19), randint(0, 19)]
Pause = False

font_small = pygame.font.SysFont('sans', 20)
font_big = pygame.font.SysFont('sans', 50)
score = 0


while running:
    clock.tick(60)
    screen.fill(BLACK)

    tail_x = snakes[0][0]
    tail_y = snakes[0][1]

    # Ve luoi
    #for i in range(21):
        #pygame.draw.line(screen, WHITE, (0,i*30), (600,i*30))
        #pygame.draw.line(screen, WHITE, (i*30,0), (i*30,600))

    # Ve ran
    for snake in snakes:
        pygame.draw.rect(screen, GREEN, (snake[0]*30, snake[1]*30, 30, 30))

    # Ve tao
    pygame.draw.rect(screen, RED, (apple[0]*30, apple[1]*30, 30, 30))

    if snakes[-1][0] == apple[0] and snakes[-1][1] == apple[1]:
        snakes.insert(0, [tail_x, tail_y])
        apple = [randint(0, 19), randint(0, 19)]
        score += 1

    # Kiem tra va cham
    if snakes[-1][0] < 0 or snakes[-1][0] >19 or snakes[-1][1] < 0 or snakes[-1][1] > 19:
        Pause = True
    

    
    
    # Hien thi diem
    Score_txt = font_small.render(f"Score: {score}", True, WHITE)
    screen.blit(Score_txt, (10, 10))

    # Xu ly su kien
    if Pause == False:
        if direction == "right":
            snakes.append([snakes[-1][0] + 1, snakes[-1][1]])
            snakes.pop(0)
        if direction == "left":
            snakes.append([snakes[-1][0] - 1, snakes[-1][1]])
            snakes.pop(0)
        if direction == "up":
            snakes.append([snakes[-1][0], snakes[-1][1] - 1])
            snakes.pop(0)
        if direction == "down":
            snakes.append([snakes[-1][0], snakes[-1][1] + 1])
            snakes.pop(0)

    # Kiem tra va cham voi than ran
    for i in range(len(snakes)-1):
        if snakes[-1][0] == snakes[i][0] and snakes[-1][1] == snakes[i][1]:
            Pause = True

    # Man hinh game over
    if Pause == True:
        Game_over_txt = font_big.render(f"Game Over, Score: {score}", True, WHITE)
        screen.blit(Game_over_txt, (50, 250))
        Press_spcae_txt = font_big.render(f"Press space to continue", True, WHITE)
        screen.blit(Press_spcae_txt, (50, 300))
    sleep(0.1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "down":
                direction = "up"
            if event.key == pygame.K_DOWN and direction != "up":
                direction = "down"
            if event.key == pygame.K_LEFT and direction != "right":
                direction = "left"
            if event.key == pygame.K_RIGHT and direction != "left":
                direction = "right"
            if event.key == pygame.K_SPACE and Pause == True:
                Pause = False
                snakes = [[5,6], [5,7]]
                direction = "right"
                apple = [randint(0, 19), randint(0, 19)]
                score = 0

    pygame.display.flip()

pygame.quit()
