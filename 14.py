import pygame
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Heart")

# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Heart function using parametric equations
def draw_heart(surface, x_offset, y_offset, size):
    points = []
    for t in range(0, 360, 1):  # Loop through angles
        rad = math.radians(t)
        x = int(size * (16 * math.sin(rad) ** 3)) + x_offset
        y = int(size * (13 * math.cos(rad) - 5 * math.cos(2 * rad) - 2 * math.cos(3 * rad) - math.cos(4 * rad))) + y_offset
        points.append((x, HEIGHT - y))  # Flip y-axis to match Pygame's coordinates

    pygame.draw.polygon(surface, RED, points)

# Main loop
running = True
while running:
    screen.fill(WHITE)
    
    draw_heart(screen, WIDTH // 2, HEIGHT // 2, 10)  # Draw the heart
    
    pygame.display.flip()  # Update the screen

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
