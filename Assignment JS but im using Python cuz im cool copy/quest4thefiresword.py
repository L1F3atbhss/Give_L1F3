import pygame
from random import randint

pygame.init()

# Game settings
WIDTH = 1400
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Quest For The Dragon Crystal")

# Game state variables
score = 0
xp = 0
game_over = False
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GROUND_COLOR = (50, 205, 50)
BUTTON_COLOR = (100, 100, 200)
HOVER_COLOR = (150, 150, 255)
BROWN = (128, 0, 0)

# Player settings
player_size = 150
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - player_size
player_speed = 5
player_velocity_y = 0
jump_height = -15
gravity = 1

# Ground settings
ground_level = HEIGHT - player_size

# Load and resize player, heart and Crystal image
player_image = pygame.image.load("WH.png")
player_image = pygame.transform.scale(player_image, (player_size, player_size))
heart_image = pygame.image.load("HP.png")
heart_image = pygame.transform.scale(heart_image, (40, 40))
Crystal = pygame.image.load("Crystal.png")
Crystal = pygame.transform.scale(Crystal, (40, 40))

# Player health and crystal count
player_health = 3
player_Crystal = 0

# Function to create a gradient
def draw_gradient(screen, color1, color2):
    for i in range(HEIGHT):
        r = color1[0] + (color2[0] - color1[0]) * i // HEIGHT
        g = color1[1] + (color2[1] - color1[1]) * i // HEIGHT
        b = color1[2] + (color2[2] - color1[2]) * i // HEIGHT
        pygame.draw.line(screen, (r, g, b), (0, i), (WIDTH, i))

# Title screen
def show_title_screen():
    running = True
    while running:
        screen.fill((0, 0, 0))
        draw_gradient(screen, (139, 70, 20), (0, 0, 0))

        # Draw title
        font = pygame.font.Font(None, 100)
        title_text = font.render("The Quest For The Dragon Crystal", True, WHITE)
        text_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 3))
        screen.blit(title_text, text_rect)

        # Draw buttons
        font = pygame.font.Font(None, 50)
        start_text = font.render("Start", True, WHITE)
        credits_text = font.render("Credits", True, WHITE)

        start_button_rect = start_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        credits_button_rect = credits_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 60))

        # Check for hovering and change color
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if start_button_rect.collidepoint(mouse_x, mouse_y):
            start_text = font.render("Start", True, HOVER_COLOR)
        if credits_button_rect.collidepoint(mouse_x, mouse_y):
            credits_text = font.render("Credits", True, HOVER_COLOR)

        screen.blit(start_text, start_button_rect)
        screen.blit(credits_text, credits_button_rect)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button_rect.collidepoint(event.pos):
                    return  # Exit title screen to start the game
                if credits_button_rect.collidepoint(event.pos):
                    show_credits()  # Display credits screen

        # Update display
        pygame.display.flip()
        clock.tick(60)

# Win screen function
def show_Win():
    running = True
    while running:
        screen.fill((0, 0, 0))
        draw_gradient(screen, (139, 70, 20), (0, 0, 0))

        # Draw title
        font = pygame.font.Font(None, 100)
        title_text = font.render("GG, You Won!", True, WHITE)
        text_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 3))
        screen.blit(title_text, text_rect)

        # Display XP and Score
        font_small = pygame.font.Font(None, 50)
        xp_text = font_small.render(f"XP: {xp}", True, WHITE)
        score_text = font_small.render(f"Score: {score}", True, WHITE)
        screen.blit(xp_text, (WIDTH // 2 - 50, HEIGHT // 2))
        screen.blit(score_text, (WIDTH // 2 - 50, HEIGHT // 2 + 50))
        

# Death screen function
def show_Death():
    font_large = pygame.font.Font(None, 80)
    font_small = pygame.font.Font(None, 50)

    # Draw the death message
    screen.fill((0, 0, 0))  # Black background
    title_text = font_large.render("You Died!", True, (255, 0, 0))  # Red text
    title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 3))
    screen.blit(title_text, title_rect)


# Credits screen function
def show_credits():
    running = True
    while running:
        screen.fill((0, 0, 0))
        draw_gradient(screen, (0, 0, 0), (139, 69, 19))  # Brown to Black background

        font = pygame.font.Font(None, 50)
        credits_text = font.render("Credits: Made by Nathan Chan", True, WHITE)
        back_text = font.render("Press G to go back", True, WHITE)

        credits_rect = credits_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 30))
        back_rect = back_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 30))

        screen.blit(credits_text, credits_rect)
        screen.blit(back_text, back_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    running = False  # Exit credits screen

        # Update display
        pygame.display.flip()
        clock.tick(60)

# Show title screen before starting the game
show_title_screen()

# X, Y, Width, Height
platforms = [
    pygame.Rect(200, 600, 300, 20),  
    pygame.Rect(600, 500, 300, 20),  
    pygame.Rect(1000, 400, 200,20), 
    pygame.Rect(600, 300, 300, 20),
    pygame.Rect(150, 200, 300, 20),
    pygame.Rect(1000, 200, 300,20)
]
#Left Door (in game)
Door = [
    pygame.Rect(10, 600, 75, 375),
    
]
#(Door Knob)
DK = [
    pygame.Rect(60, 650, 15, 10),
]

# Crystal position
crystal_rect = pygame.Rect(randint(0, WIDTH - 40), randint(100, HEIGHT - 200), 40, 40)

# timer
timer_duration = randint(30, 90) * 1000
start_time = pygame.time.get_ticks()

def draw_platforms():
    for platform in platforms:
        pygame.draw.rect(screen, BLACK, platform)

def draw_door():
    for door in Door:
        pygame.draw.rect(screen, BLACK, door)

def draw_DK():
    for TBDoor in DK:
        pygame.draw.rect(screen, BROWN, TBDoor)

# game loop
running = True
is_grounded = False  # Track if the player is on the ground or platform

# Add a variable to track if the player is flipped
is_flipped = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement and flipping
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and player_x > 0:
        player_x -= player_speed
        if not is_flipped:
            player_image = pygame.transform.flip(player_image, True, False)
            is_flipped = True
    if keys[pygame.K_d] and player_x < WIDTH - player_size:
        player_x += player_speed
        if is_flipped:
            player_image = pygame.transform.flip(player_image, True, False)
            is_flipped = False
    if keys[pygame.K_SPACE] and is_grounded:  # Only jump if grounded
        player_velocity_y = jump_height
        is_grounded = False  # The player is now in the air

    # Apply gravity
    player_velocity_y += gravity
    player_y += player_velocity_y

    # Ground collision
    if player_y > ground_level:
        player_y = ground_level
        player_velocity_y = 0
        is_grounded = True  # Player is on the ground

    # Platform collision
    for platform in platforms:
        # Check if the player is falling and intersects a platform
        if player_velocity_y > 0 and player_x + player_size > platform.left and player_x < platform.right:
            # Check if the player's bottom is above the platform's top
            if player_y + player_size <= platform.top + player_velocity_y and player_y + player_size >= platform.top:
                player_y = platform.top - player_size  # Place the player on top of the platform
                player_velocity_y = 0  # Stop downward movement
                is_grounded = True  # Player is on a platform

    # Check collision with Crystal
    if player_x < crystal_rect.right and player_x + player_size > crystal_rect.left:
        if player_y < crystal_rect.bottom and player_y + player_size > crystal_rect.top:
            player_Crystal += 1 
            score += 1
            xp = score * 100
            print("Score:", score)
            print("Xp:", xp)
            crystal_rect = pygame.Rect(randint(0, WIDTH - 40), randint(100, HEIGHT - 200), 40, 40)  # Reset crystal position

    # Clear screen and draw gradient background
    draw_gradient(screen, (0, 0, 0), (139, 69, 19))

    # Draw ground
    pygame.draw.rect(screen, GROUND_COLOR, (0, ground_level + player_size, WIDTH, HEIGHT - ground_level))

    # Draw platforms and door
    draw_platforms()
    draw_door()
    draw_DK()

    # Draw player
    screen.blit(player_image, (player_x, player_y))

    # Draw UI (hearts)
    for i in range(player_health):
        screen.blit(heart_image, (10 + i * 50, 10))

    # Draw UI (Crystal)
    for i in range(player_Crystal):
        screen.blit(Crystal, (10 + i * 50, 60))

    # Draw Crystal
    screen.blit(Crystal, crystal_rect.topleft)

    # Calculate and display timer
    elapsed_time = pygame.time.get_ticks() - start_time  # Time elapsed in milliseconds
    remaining_time = max(0, timer_duration - elapsed_time) // 1000  # Remaining time in seconds
    font = pygame.font.Font(None, 50)
    timer_text = font.render(f"Time Left: {remaining_time} seconds", True, WHITE)
    screen.blit(timer_text, (WIDTH - 250, 10))

    # Check timer expiration
    if remaining_time == 0:
        show_Death()  # Display death screen if time runs out
        running = True

    # Check for win condition
    if player_Crystal >= 10:
        show_Win()  # Display win screen
        running = True

    # Update display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
