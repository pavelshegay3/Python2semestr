import pygame
import random

pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set up the square
square_size = 50
square_x = random.randint(0, screen_width - square_size)
square_y = random.randint(0, screen_height - square_size)
square_color = (255, 0, 0)  # Red

# Set up the timer
timer = pygame.time.get_ticks()
timer_interval = 3000  # 3 seconds in milliseconds

while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Draw the square
    screen.fill((255, 255, 255))  # White background
    pygame.draw.rect(screen, square_color, (square_x, square_y, square_size, square_size))

    # Check if the timer has expired
    current_time = pygame.time.get_ticks()
    if current_time - timer >= timer_interval:
        # Change the coordinates of the square
        square_x = random.randint(0, screen_width - square_size)
        square_y = random.randint(0, screen_height - square_size)
        # Reset the timer
        timer = pygame.time.get_ticks()

    pygame.display.update()