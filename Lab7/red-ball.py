import pygame

Window_Width = 1200
Window_Hight = 720
pygame.init()
screen = pygame.display.set_mode((Window_Width, Window_Hight))
runTime = True

x = Window_Width / 2
y = Window_Hight / 2
RADIUS = 50
RED = (255, 0, 0)

clock = pygame.time.Clock()

while runTime:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        runTime = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        is_blue = not is_blue
        
        pressed = pygame.key.get_pressed()
        
        if x + RADIUS > Window_Width: x = Window_Width - RADIUS
        if x - RADIUS < 0: x = RADIUS
        if y + RADIUS > Window_Hight: y = Window_Hight - RADIUS
        if y - RADIUS < 0: y = RADIUS

        if pressed[pygame.K_UP]: y -= 20
        if pressed[pygame.K_DOWN]: y += 20
        if pressed[pygame.K_LEFT]: x -= 20
        if pressed[pygame.K_RIGHT]: x += 20
        
        screen.fill((255, 255, 255))
        pygame.draw.circle(screen, RED, (x, y), RADIUS)
        
        pygame.display.flip()
        clock.tick(60)