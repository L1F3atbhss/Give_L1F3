import cv2
import mediapipe as mp
import numpy as np
import math

# Setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
canvas = None
prev_x, prev_y = 0, 0
clear_mode = False  # Flag to prevent continuous clearing

def distance(p1, p2):
    return math.hypot(p2[0] - p1[0], p2[1] - p1[1])

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    if canvas is None:
        canvas = np.zeros_like(frame)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    draw = False
    draw_color = (0, 0, 255)  # Default to red

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            h, w, _ = frame.shape
            landmarks = hand_landmarks.landmark

            def is_finger_up(tip, pip):
                return landmarks[tip].y < landmarks[pip].y

            # Finger status
            index_up = is_finger_up(8, 6)
            middle_up = is_finger_up(12, 10)
            ring_up = is_finger_up(16, 14)
            pinky_up = is_finger_up(20, 18)
            thumb_up = landmarks[4].x < landmarks[3].x if landmarks[17].x < landmarks[5].x else landmarks[4].x > landmarks[3].x

            # Get landmark positions
            x_index = int(landmarks[8].x * w)
            y_index = int(landmarks[8].y * h)
            x_middle = int(landmarks[12].x * w)
            y_middle = int(landmarks[12].y * h)
            x_thumb = int(landmarks[4].x * w)
            y_thumb = int(landmarks[4].y * h)

            # Condition 1: Clear canvas if all fingers are up
            if index_up and middle_up and ring_up and pinky_up and thumb_up:
                if not clear_mode:
                    canvas = np.zeros_like(frame)
                    clear_mode = True
            else:
                clear_mode = False

            # Check if index or middle are touching thumb
            if distance((x_index, y_index), (x_thumb, y_thumb)) < 30:
                draw = True
                draw_color = (0, 0, 255)  # Red
            elif distance((x_middle, y_middle), (x_thumb, y_thumb)) < 30:
                draw = True
                draw_color = (255, 0, 0)  # Blue
            else:
                prev_x, prev_y = 0, 0

            # Drawing logic
            if draw:
                x_draw = x_index if draw_color == (0, 0, 255) else x_middle
                y_draw = y_index if draw_color == (0, 0, 255) else y_middle
                if prev_x == 0 and prev_y == 0:
                    prev_x, prev_y = x_draw, y_draw
                cv2.line(canvas, (prev_x, prev_y), (x_draw, y_draw), draw_color, thickness=5)
                prev_x, prev_y = x_draw, y_draw

            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    else:
        prev_x, prev_y = 0, 0

    # Overlay canvas
    alpha = 0.8
    frame = cv2.addWeighted(frame, 1 - alpha, canvas, alpha, 0)
    cv2.imshow("Virtual Drawing Board", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()