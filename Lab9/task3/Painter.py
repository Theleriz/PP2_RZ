import pygame
import math

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480)) 
    clock = pygame.time.Clock()
    
    radius = 15 
    mode = 'blue'  
    drawing_mode = 'brush'  
    points = []  
    shapes = []  # drawaed shapes
    start_pos = None #start position 

    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        #handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return

                # change color
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_e:
                    drawing_mode = 'eraser'  

                #shape coice
                elif event.key == pygame.K_t:
                    drawing_mode = 'rect'  
                elif event.key == pygame.K_c:
                    drawing_mode = 'circle'  
                elif event.key == pygame.K_s:
                    drawing_mode = 'square' 
                elif event.key == pygame.K_y:
                    drawing_mode = 'right_triangle' 
                elif event.key == pygame.K_u:
                    drawing_mode = 'equilateral_triangle' 
                elif event.key == pygame.K_h:
                    drawing_mode = 'rhombus'  
            #handle mouse control
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  
                    start_pos = event.pos

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and start_pos:
                    end_pos = event.pos
                    shapes.append((drawing_mode, start_pos, end_pos, mode))  
                    start_pos = None

        screen.fill((0, 0, 0))  

        #draw shapes from list
        for shape in shapes:
            draw_shape(screen, shape[0], shape[1], shape[2], shape[3])

        pygame.display.flip()
        clock.tick(60)

def draw_shape(screen, shape_type, start, end, mode):
    color = get_color(mode)
    if shape_type == 'rect':
        pygame.draw.rect(screen, color, (*start, end[0] - start[0], end[1] - start[1]), 2)
    elif shape_type == 'circle':
        radius = int(math.dist(start, end)) #update radius
        pygame.draw.circle(screen, color, start, radius, 2)
    elif shape_type == 'square':
        side = min(abs(end[0] - start[0]), abs(end[1] - start[1]))  
        pygame.draw.rect(screen, color, (*start, side, side), 2)
    elif shape_type == 'right_triangle':
        pygame.draw.polygon(screen, color, [start, (start[0], end[1]), end], 2)
    elif shape_type == 'equilateral_triangle':
        side = abs(end[0] - start[0])
        height = int(side * math.sqrt(3) / 2)
        pygame.draw.polygon(screen, color, [start, (start[0] + side, start[1]), (start[0] + side // 2, start[1] - height)], 2)
    elif shape_type == 'rhombus':
        dx = abs(end[0] - start[0]) // 2
        dy = abs(end[1] - start[1]) // 2
        pygame.draw.polygon(screen, color, [(start[0], start[1] - dy), (start[0] + dx, start[1]),
                                            (start[0], start[1] + dy), (start[0] - dx, start[1])], 2)

def get_color(mode):
    colors = {'blue': (0, 0, 255), 'red': (255, 0, 0), 'green': (0, 255, 0)}
    return colors.get(mode, (255, 255, 255))  

main()

# Управление:
# R, G, B — color choice
# E — eraser
# T — rectangle
# C — circle
# S — square
# Y — right rectangle
# U — right triangle
# H — rhombus   
# LeftMouseButton - to start draw

