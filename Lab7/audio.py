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
            runtime = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if is_playing:
                    pygame.mixer.music.pause()
                    is_playing = False
                else:
                    pygame.mixer.music.unpause()
                    is_playing = True

            elif event.key == pygame.K_RIGHT:
                pygame.mixer.music.stop()
                index = (index + 1) % len(music_list)
                song = os.path.join(folder, music_list[index])
                pygame.mixer.music.load(song)
                pygame.mixer.music.play()
                is_playing = True

            elif event.key == pygame.K_LEFT:
                pygame.mixer.music.stop()
                index = (index - 1) % len(music_list)
                song = os.path.join(folder, music_list[index])
                pygame.mixer.music.load(song)
                pygame.mixer.music.play()
                is_playing = True

    pygame.display.flip()
    pygame.time.Clock().tick(60)

#разобраться с нажатиям несколько раз сразу

pygame.quit()
