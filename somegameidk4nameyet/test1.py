import cv2
import mediapipe as mp
import math

def calculate_angle(a, b, c):
    """ Calculate the angle between three points """
    ang = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0]) - 
                       math.atan2(a[1]-b[1], a[0]-b[0]))
    return abs(ang) if abs(ang) <= 180 else 360 - abs(ang)

# Initialize mediapipe hands module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=5, model_complexity=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

finger_tips_ids = [4, 8, 12, 16, 20]

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    h, w, c = frame.shape

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks and results.multi_handedness:
        for hand_landmarks, hand_handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
            lm_list = []

            label = hand_handedness.classification[0].label  # Left or Right

            for id, lm in enumerate(hand_landmarks.landmark):
                lm_list.append((int(lm.x * w), int(lm.y * h)))

            fingers_up = []

            # Thumb using angle
            thumb_angle = calculate_angle(lm_list[2], lm_list[3], lm_list[4])
            if thumb_angle > 160:
                fingers_up.append(1)
            else:
                fingers_up.append(0)

            # Other 4 fingers
            for id in range(1, 5):
                if lm_list[finger_tips_ids[id]][1] < lm_list[finger_tips_ids[id] - 2][1]:
                    fingers_up.append(1)
                else:
                    fingers_up.append(0)

            # Draw landmarks
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Show finger count
            total_fingers = fingers_up.count(1)
            wrist_x, wrist_y = lm_list[0]

            # Draw label
            cv2.putText(frame, f'{label} Hand: {total_fingers}', (wrist_x - 50, wrist_y - 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

    cv2.imshow("Multi-Hand Finger Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()