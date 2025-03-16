import pygame
import os


pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((400, 300))
folder = 'folder'
music_list = [song for song in os.listdir(folder) if song.endswith('.mp3')]
index = 0
runtime = True
is_playing = True


song = os.path.join(folder, music_list[index])
pygame.mixer.music.load(song)
pygame.mixer.music.play()
    
while runtime:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
        break

    if keys[pygame.K_SPACE]:
        if is_playing:
            pygame.mixer.music.stop()
            is_playing = False
        else:
            pygame.mixer.music.play()
            
            

    elif keys[pygame.K_RIGHT]:
        pygame.mixer.music.stop()
        index += 1 % len(music_list)
        song = os.path.join(folder, music_list[index % len(music_list)])
        pygame.mixer.music.load(song)
        pygame.mixer.music.play()


    elif keys[pygame.K_LEFT]:
        pygame.mixer.music.stop()
        index -= 1 % len(music_list)
        song = os.path.join(folder, music_list[index % len(music_list)])
        pygame.mixer.music.load(song)
        pygame.mixer.music.play()

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()