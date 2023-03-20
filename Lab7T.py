import pygame
import os

pygame.init()
pygame.mixer.init()
monitor = pygame.display.set_mode((1600, 900))
pygame.display.set_caption('Music Player')
pygame.display.set_icon(pygame.image.load('IGRA/PICTURES/5898870_console_device_game_play_icon.png'))
font = pygame.font.Font('IGRA/FONTS/Anton-Regular.ttf', 40)
font2 = pygame.font.Font('IGRA/FONTS/Anton-Regular.ttf', 25)
text = font.render('CONTROLS', False, "White")
text2 = font2.render('Play - W', False, "White")
text3 = font2.render('Stop - S', False, "White")
text4 = font2.render('Next - D', False, "White")
text5 = font2.render('Previous - A', False, "White")
text6 = font.render('Current track: ', False, "White")
text7 = font.render('Status: ', False, 'White')
text8='Paused'
text9= font.render(text8, False, 'White')
direct = "IGRA/SOUNDS/"
tracks = ["02 Entry Screen.mp3", "03 Terraformer.mp3", "04 Moving On.mp3", "05 I Like It Here.mp3"]
i = c = 0
trt = tracks[i]
pygame.mixer.music.load(os.path.join(direct, tracks[i]))
check = True
while check:
    monitor.fill((98, 166, 126))
    monitor.blit(text, (100, 120))
    monitor.blit(text2, (100, 200))
    monitor.blit(text3, (100, 250))
    monitor.blit(text4, (100, 300))
    monitor.blit(text5, (100, 350))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and c == 0:
                pygame.mixer.music.play()
                c = 1
            if event.key == pygame.K_w and c == 1:
                pygame.mixer.music.unpause()
            if event.key == pygame.K_s and c == 1:
                pygame.mixer.music.pause()
            if event.key == pygame.K_d:
                pygame.mixer.music.stop()
                if i == 3:
                    i = 0
                    pygame.mixer.music.load(os.path.join(direct, tracks[i]))
                    pygame.mixer.music.play()
                else:
                    i = i + 1
                    pygame.mixer.music.load(os.path.join(direct, tracks[i]))
                    pygame.mixer.music.play()
            if event.key == pygame.K_a:
                pygame.mixer.music.stop()
                if i == 0:
                    i = 3
                    pygame.mixer.music.load(os.path.join(direct, tracks[i]))
                    pygame.mixer.music.play()
                else:
                    i = i - 1
                    pygame.mixer.music.load(os.path.join(direct, tracks[i]))
                    pygame.mixer.music.play()

        if event.type == pygame.QUIT:
            check = False
            pygame.quit()
