import pygame, time, random

pygame.init()
H = 600
W = 800
dis = pygame.display.set_mode((W, H))
pygame.display.set_caption('ZMEYA')

blue = (0, 0, 255)
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)
yellow = (255, 255, 102)
green = (0, 255, 0)
level = 1
snake_block = 10
snake_speed = 15
clock = pygame.time.Clock()
font_style = pygame.font.SysFont(None, 50)


def levels(level):
    value = font_style.render("Level: " + str(level), True, black)
    dis.blit(value, [165, 0])


def levelsend(level):
    value = font_style.render("Level Reached: " + str(level), True, white)
    dis.blit(value, [250, 0])


def respres(score):
    value = font_style.render("Score: " + str(score), True, black)
    dis.blit(value, [0, 0])


def death(why):
    reason = font_style.render("Death caused by: " + why, True, white)
    dis.blit(reason, [0, 45])


def res(score):
    value = font_style.render("Your score: " + str(score), True, white)
    dis.blit(value, [0, 0])


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, white, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [W / 2 - 350, H / 2 - 50])

def gameLoop(level, snake_speed):
    game_over = False
    game_close = False
    x1 = W / 2
    y1 = H / 2
    x1_change = 0
    y1_change = 0
    snake_list = []
    Length = 1
    foodx = round(random.randrange(0, W - snake_block) / 10) * 10
    foody = round(random.randrange(50, H - snake_block) / 10) * 10
    foodx2 = round(random.randrange(0, W - snake_block) / 10) * 10
    foody2 = round(random.randrange(50, H - snake_block) / 10) * 10
    while not game_over:
        while game_close == True:
            dis.fill(black)
            message("YOU LOST! Press Q to quit, C to play again", red)
            res(Length - 1)
            levelsend(level)
            death(why)

            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        level = 1
                        snake_speed = 15
                        gameLoop(level, snake_speed)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
        if x1 >= W or x1 < 0 or y1 >= H or y1 < H - 550:
            game_close = True
            why = 'hitting borders'
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        pygame.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block])
        if level == 2:
            pygame.draw.rect(dis, green, [foodx2, foody2, snake_block, snake_block])
        if level == 3:
            pygame.draw.rect(dis, green, [foodx2, foody2, snake_block, snake_block])
        if level == 4:
            pygame.draw.rect(dis, green, [foodx2, foody2, snake_block, snake_block])
        if level == 5:
            pygame.draw.rect(dis, green, [foodx2, foody2, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_list.append(snake_Head)
        if len(snake_list) > Length:
            del snake_list[0]
        for x in snake_list[:-1]:
            if x == snake_Head:
                game_close = True
                why = 'hitting yourself'
        pygame.draw.rect(dis, white, pygame.Rect(0, 0, W, H - 550))
        respres(Length - 1)

        # levels
        if Length - 1 in range(3, 6) and level == 1:
            level += 1
            snake_speed = 20
        elif Length - 1 in range(6, 9) and level == 2:
            level += 1
            snake_speed = 25
        elif Length - 1 in range(9, 12) and level == 3:
            level += 1
            snake_speed = 30
        elif Length - 1 in range(12, 15) and level == 4:
            level += 1
            snake_speed = 35
        elif Length - 1 in range(15, 18) and level == 5:
            level += 1
            snake_speed = 40
        levels(level)

        our_snake(snake_block, snake_list)
        pygame.display.update()
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, W - snake_block) / 10) * 10
            foody = round(random.randrange(50, H - snake_block) / 10) * 10
            Length += 1
            print("Yummy")
        if x1 == foodx2 and y1 == foody2:
            foodx2 = round(random.randrange(0, W - snake_block) / 10) * 10
            foody2 = round(random.randrange(50, H - snake_block) / 10) * 10
            Length += 3
            print("YUMMY!!!")

        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop(level, snake_speed)
