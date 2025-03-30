import pygame
import random

pygame.init()

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#variables
score = 0
fruit_eaten = False
level = 0
snake_speed = 10

def spawn_fruit():
    x = random.randrange(1, SCREEN_WIDTH // 10) * 10
    y = random.randrange(1, SCREEN_HEIGHT // 10) * 10

    return [x, y]

fruit_cooardinates = spawn_fruit()
fruit_timer = 10000 #fuit timer
fruit_spawn_time = pygame.time.get_ticks()

#snake head and body
head_square = [100, 100]
squares = [
    [30, 100],
    [40, 100], 
    [50, 100], 
    [60, 100],
    [70, 100], 
    [80, 100], 
    [90, 100], 
    [100, 100]
]

direction = "right"
next_dir = "right"

done = False

#game over
def game_over():
    global done
    font = pygame.font.SysFont("times new roman", 18)
    surface = font.render(f"Game Over, your score: {score}", True, (128, 128, 128))
    rect = surface.get_rect()
    screen.blit(surface, rect)
    pygame.display.update()
    pygame.time.delay(4000)
    done = True
    pygame.quit()

while not done:
    #handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #hanlde key downs order to controll the snake
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                next_dir = "down"
            if event.key == pygame.K_UP:
                next_dir = "up"
            if event.key == pygame.K_LEFT:
                next_dir = "left"
            if event.key == pygame.K_RIGHT:
                next_dir = "right"

    #check if head meet with body
    for square in squares[:-1]:
        if head_square == square:
            game_over()

    #check boundaries
    if head_square[0] < 0 or head_square[0] >= SCREEN_WIDTH or head_square[1] < 0 or head_square[1] >= SCREEN_HEIGHT:
        game_over()

    #update movement direction
    if next_dir == "right" and direction != "left":
        direction = "right"
    if next_dir == "up" and direction != "down":
        direction = "up"
    if next_dir == "left" and direction != "right":
        direction = "left"
    if next_dir == "down" and direction != "up":
        direction = "down"

    #snake movement
    if direction == "right":
        head_square[0] += snake_speed
    if direction == "left":
        head_square[0] -= snake_speed
    if direction == "up":
        head_square[1] -= snake_speed
    if direction == "down":
        head_square[1] += snake_speed

    #save old coordinates
    new_square = [head_square[0], head_square[1]]
    #update coordinates
    squares.append(new_square)
    squares.pop(0)

    if head_square == fruit_cooardinates:
        fruit_eaten = True
        score += 5 #add score
        
    #level logic
    match score:
        case 25:
            level = 1
            #snake_speed = 15
        case 50:
            level = 2
            #snake_speed = 35
        case 75:
            level = 3
            #snake_speed = 50


    #respawn fruit
    if fruit_eaten or pygame.time.get_ticks() - fruit_spawn_time > fruit_timer:
        fruit_cooardinates = spawn_fruit()
        fruit_spawn_time = pygame.time.get_ticks()
        fruit_eaten = False

    screen.fill((0, 0, 0))

    font = pygame.font.SysFont("times new roman", 20)
    score_surface = font.render(f"Score: {score}" , True, (128, 128, 128)) #display score
    level_display = font.render(f"level: {level}", True, (128, 128, 128))
    screen.blit(score_surface, (10, 10))
    screen.blit(level_display, (220, 10))

    if not fruit_eaten:
        pygame.draw.circle(screen, (255, 0, 0), (fruit_cooardinates[0] + 5, fruit_cooardinates[0] + 5), 5)

    for el in squares:
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(el[0], el[1], 10, 10))

    pygame.display.flip()
    pygame.time.delay(200)

pygame.quit()