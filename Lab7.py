import pygame

pygame.init()
monitor = pygame.display.set_mode((1600, 900))
pygame.display.set_caption('mygame')
pygame.display.set_icon(pygame.image.load('IGRA/PICTURES/5898870_console_device_game_play_icon.png'))
font = pygame.font.Font('IGRA/FONTS/Anton-Regular.ttf', 25)
text = font.render('this is a game', False, "White")
image = pygame.image.load('IGRA/PICTURES/5898870_console_device_game_play_icon.png')
image=pygame.transform.scale(image,(150,150))


check = True
background=pygame.image.load("IGRA/PICTURES/EGS_RimWorld_LudeonStudios_S1-2560x1440-410a62ec21d44260409182e1174cce2e.jpg")
background = pygame.transform.scale(background, (1600, 900))
sound=pygame.mixer.Sound('IGRA/SOUNDS/02 Entry Screen.mp3')
sound.play()
sound.set_volume(0.1)
while check:
    monitor.fill((98, 166, 126))
    monitor.blit(background,(0,0))
    pygame.draw.circle(monitor, (98, 166, 126), (30, 800), 20)
    monitor.blit(text, (100, 100))
    monitor.blit(image, (1025, 300))
    pygame.display.update()
    for action in pygame.event.get():
        if action.type == pygame.QUIT:
            check = False
            pygame.quit()
