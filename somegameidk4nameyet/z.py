import cv2
import mediapipe as mp
import pygame
import sys
import math
import numpy as np

# Initialize Pygame
pygame.init()
WIDTH = 1350
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('GameZ')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Box position and speed
box_x, box_y = 50, 50
box_size = 100

# RED Box position and size
REDbox_x, REDbox_y = 50, 50
REDbox_size = 100

# Initialize MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, model_complexity=1, min_detection_confidence=0.7)

# Webcam
cap = cv2.VideoCapture(0)
cam_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
cam_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

clock = pygame.time.Clock()
running = True
DIE = False

# Smoothed finger position history
index_history = []

def smooth_position(new_pos, history, size=5):
    history.append(new_pos)
    if len(history) > size:
        history.pop(0)
    avg_x = sum(p[0] for p in history) / len(history)
    avg_y = sum(p[1] for p in history) / len(history)
    return int(avg_x), int(avg_y)

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            lm = hand_landmarks.landmark

            # Get index and thumb tip positions
            index_x = int(lm[8].x * WIDTH)
            index_y = int(lm[8].y * HEIGHT)
            thumb_x = int(lm[4].x * WIDTH)
            thumb_y = int(lm[4].y * HEIGHT)

            # Distance between thumb and index
            distance = math.hypot(index_x - thumb_x, index_y - thumb_y)

            # Only move if fingers are close (like a pinch)
            if distance < 40:
                smoothed_x, smoothed_y = smooth_position((index_x, index_y), index_history)

                # Move box towards the index finger smoothly
                dx = smoothed_x - (box_x + box_size // 2)
                dy = smoothed_y - (box_y + box_size // 2)

                box_x += int(dx * 0.2)
                box_y += int(dy * 0.2)
            else:
                index_history.clear()  # reset history if fingers are apart

    def redBox():
        pygame.draw.rect(screen, RED, (REDbox_x, REDbox_y, REDbox_size, REDbox_size))

    redBox()

    # Clamp to screen bounds
    box_x = max(0, min(WIDTH - box_size, box_x))
    box_y = max(0, min(HEIGHT - box_size, box_y))

    # Draw box
    pygame.draw.rect(screen, BLACK, (box_x, box_y, box_size, box_size))
    pygame.display.update()
    clock.tick(30)

# Cleanup
cap.release()
cv2.destroyAllWindows()
pygame.quit()
sys.exit()