import pygame

pygame.init()
monitor = pygame.display.set_mode((1600, 900))
pygame.display.set_caption('moving circle')
pygame.display.set_icon(pygame.image.load('IGRA/PICTURES/5898870_console_device_game_play_icon.png'))
font = pygame.font.Font('IGRA/FONTS/Anton-Regular.ttf', 25)
text = font.render('this is a game', False, "Black")
image = pygame.image.load('IGRA/PICTURES/5898870_console_device_game_play_icon.png')
image = pygame.transform.scale(image, (150, 150))
bsize = 50
brad = 25
bx = (1600 - 50) / 2
by = (800 - 50) / 2
bspeed = 20

check = True
sound = pygame.mixer.Sound('IGRA/SOUNDS/02 Entry Screen.mp3')
sound.play()
sound.set_volume(0.1)
while check:
    monitor.blit(text, (100, 100))
    monitor.blit(image, (1025, 300))
    pygame.display.update()
    for action in pygame.event.get():
        if action.type == pygame.KEYDOWN:
            if action.key == pygame.K_UP:
                by = by - bspeed
            if action.key == pygame.K_DOWN:
                by = by + bspeed
            if action.key == pygame.K_RIGHT:
                bx = bx + bspeed
            if action.key == pygame.K_LEFT:
                bx = bx - bspeed

        if action.type == pygame.QUIT:
            check = False
            pygame.quit()
    if bx < 0:
        bx = 0
    if by < 0:
        by = 0
    if bx > 1600 - 50:
        bx = 1600 - 50
    if by > 900 - 50:
        by = 900 - 50
    monitor.fill("White")
    pygame.draw.circle(monitor, "Red", (bx + brad, by + brad), brad)
    monitor.blit(text, (100, 100))
    monitor.blit(image, (1025, 300))
    pygame.display.update()
