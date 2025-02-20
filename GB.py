import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Burger Falling on School!')

# Define colors
WHITE = (255, 255, 255)

# Load images
burger_img = pygame.image.load('burger.png')
school_bg = pygame.image.load('school_background.avif')

# Scale the images if needed
burger_img = pygame.transform.scale(burger_img, (50, 50))
school_bg = pygame.transform.scale(school_bg, (screen_width, screen_height))

# Burger settings
burger_x = random.randint(0, screen_width - 50)
burger_y = -50
burger_speed = 5

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update burger position
    burger_y += burger_speed
    if burger_y > screen_height:
        burger_y = -50
        burger_x = random.randint(0, screen_width - 50)

    # Draw everything
    screen.fill(WHITE)
    screen.blit(school_bg, (0, 0))  # Draw the school background
    screen.blit(burger_img, (burger_x, burger_y))  # Draw the falling burger

    # Update the screen
    pygame.display.flip()

    # Delay to make the game run at a reasonable speed
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()