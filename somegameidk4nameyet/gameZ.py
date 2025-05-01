import cv2
import mediapipe as mp
import pygame
import sys
import math

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 1300, 750
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('GameZ')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Box position and speed
box_x, box_y = 50, 50
box_size = 100
speed = 10

# Initialize MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, model_complexity=1, min_detection_confidence=0.7)

# Webcam
cap = cv2.VideoCapture(0)

clock = pygame.time.Clock()
running = True

# Track previous index finger position
prev_index_x, prev_index_y = None, None

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
            h, w, _ = frame.shape

            # Get index and thumb tip positions
            index_x = int(lm[8].x * w)
            index_y = int(lm[8].y * h)
            thumb_x = int(lm[4].x * w)
            thumb_y = int(lm[4].y * h)

            # Distance between thumb and index
            distance = math.hypot(index_x - thumb_x, index_y - thumb_y)

            # Only move if fingers are touching
            if distance < 30:
                if prev_index_x is not None and prev_index_y is not None:
                    move_x = index_x - prev_index_x
                    move_y = index_y - prev_index_y

                    # Apply threshold to avoid jitter
                    if abs(move_x) > 5:
                        box_x += speed if move_x > 0 else -speed
                    if abs(move_y) > 5:
                        box_y += speed if move_y > 0 else -speed

                # Update previous index finger position
                prev_index_x = index_x
                prev_index_y = index_y
            else:
                prev_index_x, prev_index_y = None, None  # reset if not touching

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