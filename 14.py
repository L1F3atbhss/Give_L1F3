import pygame
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("<3 ")

# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Heart function using parametric equations
def get_heart_points(x_offset, y_offset, size):
    points = []
    for t in range(0, 360, 1):  # Loop through angles
        rad = math.radians(t)
        x = int(size * (16 * math.sin(rad) ** 3)) + x_offset
        y = int(size * (13 * math.cos(rad) - 5 * math.cos(2 * rad) - 2 * math.cos(3 * rad) - math.cos(4 * rad))) + y_offset
        points.append((x, HEIGHT - y))  # Flip y-axis to match Pygame's coordinates
    return points

# Get heart shape points
heart_points = get_heart_points(WIDTH // 2, HEIGHT // 2, 10)

# Main loop
running = True
drawn_points = []
clock = pygame.time.Clock()
index = 0

while running:
    screen.fill(WHITE)
    
    # Draw the heart gradually
    if index < len(heart_points):
        drawn_points.append(heart_points[index])
        index += 1

    if len(drawn_points) > 1:
        pygame.draw.lines(screen, RED, False, drawn_points, 3)

    pygame.display.flip()
    clock.tick(45)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()