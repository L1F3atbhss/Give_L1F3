import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Music Player")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHTBLUE = (180, 215, 230)

# Fonts
font = pygame.font.Font(None, 50)

# Utility to draw text
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x, y))
    surface.blit(text_obj, text_rect)

# Button class
class Button:
    def __init__(self, x, y, width, height, color, text_color, text, action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text_color = text_color
        self.text = text
        self.action = action

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        draw_text(self.text, font, self.text_color, surface, self.rect.centerx, self.rect.centery)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

# Load and play music
def play_music(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.set_volume(0.5)  # Adjust volume (0.0 to 1.0)
    pygame.mixer.music.play(-1)  # Loop the music indefinitely

# Stop the music
def stop_music():
    pygame.mixer.music.stop()

# Main screen
def main_screen():
    play_button = Button(200, 200, 400, 100, LIGHTBLUE, BLACK, "Play Music", play_music)
    stop_button = Button(200, 350, 400, 100, LIGHTBLUE, BLACK, "Stop Music", stop_music)

    while True:
        mouse_pos = pygame.mouse.get_pos()
        screen.fill(WHITE)

        # Draw buttons
        play_button.draw(screen)
        stop_button.draw(screen)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.is_clicked(mouse_pos):
                    play_button.action("calm_music.mp3")  # Replace with your music file path
                if stop_button.is_clicked(mouse_pos):
                    stop_button.action()

        # Draw title
        draw_text("Simple Music Player", font, BLACK, screen, WIDTH // 2, 100)

        pygame.display.update()

# Start the program
if __name__ == "__main__":
    main_screen()