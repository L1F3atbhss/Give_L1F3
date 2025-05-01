import cv2
import mediapipe as mp
import pygame
import sys
import math

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 1300, 750
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Stable Hand Controlled Box')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Box position and speed
box_x, box_y = 50, 50
box_size = 100
speed = 50  # one large step per gesture

# Gesture state
pinch_active = False

# MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, model_complexity=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
clock = pygame.time.Clock()
running = True

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

            thumb_x = int(lm[4].x * w)
            thumb_y = int(lm[4].y * h)
            index_x = int(lm[8].x * w)
            index_y = int(lm[8].y * h)

            dx = index_x - thumb_x
            dy = index_y - thumb_y
            distance = math.hypot(dx, dy)

            pinch_threshold = 40  # pixels

            if distance < pinch_threshold and not pinch_active:
                pinch_active = True  # Activate only once per pinch

                # Determine direction
                if abs(dx) > abs(dy):
                    if dx > 0:
                        box_x += speed
                    else:
                        box_x -= speed
                else:
                    if dy > 0:
                        box_y += speed
                    else:
                        box_y -= speed

            elif distance >= pinch_threshold:
                pinch_active = False  # Reset once fingers are apart again

    # Clamp to screen bounds
    box_x = max(0, min(WIDTH - box_size, box_x))
    box_y = max(0, min(HEIGHT - box_size, box_y))

    # Draw the box
    pygame.draw.rect(screen, BLACK, (box_x, box_y, box_size, box_size))
    pygame.display.update()
    clock.tick(30)

# Cleanup
cap.release()
cv2.destroyAllWindows()
pygame.quit()
sys.exit()