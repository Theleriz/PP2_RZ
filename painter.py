import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    mode = 'blue'
    points = []
    draw_mode = 'erase'
    
    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and (
                (event.key == pygame.K_w and ctrl_held) or 
                (event.key == pygame.K_F4 and alt_held) or 
                (event.key == pygame.K_ESCAPE))):
                return
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_e:
                    draw_mode = 'erase'
                elif event.key == pygame.K_c:
                    draw_mode = 'circle'
                elif event.key == pygame.K_t:
                    draw_mode = 'rectangle'
            
            if event.type == pygame.MOUSEMOTION:
                position = event.pos
                points.append(position)
                points = points[-256:]
                
        screen.fill((0, 0, 0))
        
        for i in range(len(points) - 1):
            if draw_mode == 'circle':
                drawCircle(screen, i, points[i], points[i + 1], radius, mode)
            elif draw_mode == 'rectangle':
                drawRectangle(screen, i, points[i], points[i + 1], mode)
            elif draw_mode == 'erase':
                Eraser(screen, points[i], points[i + 1], radius)
        
        pygame.display.flip()
        clock.tick(60)

def drawRectangle(screen, index, start, end, color_mode):
    color = getColor(index, color_mode)
    dx, dy = start[0] - end[0], start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = i / iterations
        x, y = int((1 - progress) * start[0] + progress * end[0]), int((1 - progress) * start[1] + progress * end[1])
        pygame.draw.rect(screen, color, (x, y, 15, 15))

def drawCircle(screen, index, start, end, width, color_mode):
    color = getColor(index, color_mode)
    dx, dy = start[0] - end[0], start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = i / iterations
        x, y = int((1 - progress) * start[0] + progress * end[0]), int((1 - progress) * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

def Eraser(screen, start, end, width):
    dx, dy = start[0] - end[0], start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = i / iterations
        x, y = int((1 - progress) * start[0] + progress * end[0]), int((1 - progress) * start[1] + progress * end[1])
        pygame.draw.circle(screen, (0, 0, 0), (x, y), width)

def getColor(index, mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    if mode == 'blue':
        return (c1, c1, c2)
    elif mode == 'red':
        return (c2, c1, c1)
    elif mode == 'green':
        return (c1, c2, c1)
    return (255, 255, 255)

main()
