import cv2
import mediapipe as mp

# Initialize mediapipe hands module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2)  # Allow up to 2 hands
mp_draw = mp.solutions.drawing_utils

# Tips of each finger (based on Mediapipe hand landmark index)
finger_tips_ids = [4, 8, 12, 16, 20]

# Start webcam
cap = cv2.VideoCapture(0)  # 0 = default webcam

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)  # Mirror image
    h, w, c = frame.shape

    # Convert BGR image to RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the image and find hands
    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            lm_list = []
            fingers_up = []

            # Collect all landmark positions
            for id, lm in enumerate(hand_landmarks.landmark):
                lm_list.append((int(lm.x * w), int(lm.y * h)))

            # Thumb (special case: horizontal check)
            if lm_list[finger_tips_ids[0]][0] > lm_list[finger_tips_ids[0] - 1][0]:
                fingers_up.append(1)
            else:
                fingers_up.append(0)

            # Other 4 fingers (vertical check)
            for id in range(1, 5):
                if lm_list[finger_tips_ids[id]][1] < lm_list[finger_tips_ids[id] - 2][1]:
                    fingers_up.append(1)
                else:
                    fingers_up.append(0)

            # Draw hand landmarks
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Show number of fingers for this hand
            total_fingers = fingers_up.count(1)

            # Draw text near wrist (landmark 0 = wrist)
            wrist_x, wrist_y = lm_list[0]
            cv2.putText(frame, f'Fingers: {total_fingers}', (wrist_x - 50, wrist_y - 20), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Multi-Hand Finger Recognition", frame)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()