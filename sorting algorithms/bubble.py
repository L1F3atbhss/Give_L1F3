import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Constants
WIDTH = 800
HEIGHT = 800
BAR_WIDTH = 5
ARRAY_SIZE = WIDTH // BAR_WIDTH
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0,255,0)

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bubble Sort Visualization")
clock = pygame.time.Clock()

# Generate random array
array = [random.randint(10, HEIGHT) for _ in range(ARRAY_SIZE)]
#array = [590, 230, 10, 470, 350, 710, 190, 630, 550, 270, 430, 310, 150, 670, 510, 390, 90, 750, 710, 110, 350, 470, 270, 230, 430, 150, 310, 510, 670, 750, 90, 10, 190, 390, 550, 630, 710]

def draw_array(highlight_index=None):
    screen.fill(WHITE)
    for i, val in enumerate(array):
        color = RED if i == highlight_index else BLUE
        pygame.draw.rect(screen, color, (i * BAR_WIDTH, HEIGHT - val, BAR_WIDTH, val))
    pygame.display.update()

def bubble_sort():
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            draw_array(j)
            pygame.time.delay(10)  # Slow down for visibility
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
    draw_array()

# Main loop
running = True
sorted_flag = False
while running:
    clock.tick(FPS)
    draw_array()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not sorted_flag:
        bubble_sort()
        sorted_flag = True

pygame.quit()