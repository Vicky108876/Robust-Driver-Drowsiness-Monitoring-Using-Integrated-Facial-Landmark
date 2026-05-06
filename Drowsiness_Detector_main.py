import cv2
import joblib
import mediapipe as mp
import numpy as np
import pandas as pd
import pygame
from collections import deque
from math import hypot
import datetime

# -----------------------------
# 1. Pygame Setup (Audio Alert)
# -----------------------------
pygame.mixer.init()
try:
    alert_sound = pygame.mixer.Sound("./Sounds/Alert-sound.Mp3")
except:
    print("Warning: Alert sound file not found.")
    alert_sound = None

# -----------------------------
# 2. Load Models
# -----------------------------
mlp = joblib.load("./Models/mlp_model_v2.pkl")
scaler = joblib.load("./Models/scaler_v2.pkl")
le = joblib.load("./Models/label_map_v2.pkl")

# -----------------------------
# 3. MediaPipe Setup
# -----------------------------
mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

face_mesh = mp_face_mesh.FaceMesh(max_num_faces=1)

mp_selfie = mp.solutions.selfie_segmentation
selfie = mp_selfie.SelfieSegmentation(model_selection=1)

EAR_buf = deque(maxlen=15)
MAR_buf = deque(maxlen=15)

# -----------------------------
# 4. Video Capture
# -----------------------------
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    h, w = frame.shape[:2]
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    res = face_mesh.process(rgb_frame)

    drowsy_state = "Scanning..."
    head_state = "Detecting..."
    head_color = (255, 255, 255)
    cur_ear, cur_mar = 0.0, 0.0

    if res.multi_face_landmarks:
        face_landmarks = res.multi_face_landmarks[0]
        lm = face_landmarks.landmark

        # -----------------------------
        # Bounding Box
        # -----------------------------
        x_coords = [int(point.x * w) for point in lm]
        y_coords = [int(point.y * h) for point in lm]

        x_min, x_max = min(x_coords), max(x_coords)
        y_min, y_max = min(y_coords), max(y_coords)

        cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)

        # -----------------------------
        # FaceMesh Drawing
        # -----------------------------
        mp_drawing.draw_landmarks(
            frame,
            face_landmarks,
            mp_face_mesh.FACEMESH_CONTOURS,
            mp_drawing.DrawingSpec(color=(0,255,0), thickness=1, circle_radius=1),
            mp_drawing.DrawingSpec(color=(0,0,255), thickness=1)
        )

        # -----------------------------
        # Head Pose (Rule-Based)
        # -----------------------------
        nose = (int(lm[1].x * w), int(lm[1].y * h))
        f_left = (int(lm[234].x * w), int(lm[234].y * h))
        f_right = (int(lm[454].x * w), int(lm[454].y * h))
        f_top = (int(lm[10].x * w), int(lm[10].y * h))
        f_bottom = (int(lm[152].x * w), int(lm[152].y * h))

        h_ratio = hypot(nose[0]-f_left[0], nose[1]-f_left[1]) / (hypot(nose[0]-f_right[0], nose[1]-f_right[1]) + 1e-6)
        v_ratio = hypot(nose[0]-f_top[0], nose[1]-f_top[1]) / (hypot(nose[0]-f_bottom[0], nose[1]-f_bottom[1]) + 1e-6)

        if h_ratio > 2.2:
            head_state, head_color = "LOOKING RIGHT", (0, 0, 255)
        elif h_ratio < 0.45:
            head_state, head_color = "LOOKING LEFT", (0, 0, 255)
        elif v_ratio > 1.5:
            head_state, head_color = "LOOKING DOWN", (0, 0, 255)
        elif v_ratio < 0.6:
            head_state, head_color = "LOOKING UP", (0, 0, 255)
        else:
            head_state, head_color = "FORWARD (OK)", (0, 255, 0)

        # -----------------------------
        # EAR Calculation
        # -----------------------------
        def get_ear(eye_idx):
            pts = [(int(lm[i].x*w), int(lm[i].y*h)) for i in eye_idx]
            v = hypot(pts[1][0]-pts[5][0], pts[1][1]-pts[5][1]) + \
                hypot(pts[2][0]-pts[4][0], pts[2][1]-pts[4][1])
            h_d = hypot(pts[0][0]-pts[3][0], pts[0][1]-pts[3][1])
            return v / (2.0 * h_d + 1e-6)

        cur_ear = (get_ear([33,160,158,133,153,144]) +
                   get_ear([362,385,387,263,373,380])) / 2.0

        cur_mar = hypot(lm[13].x-lm[14].x, lm[13].y-lm[14].y) / \
                  (hypot(lm[78].x-lm[308].x, lm[78].y-lm[308].y) + 1e-6)

        EAR_buf.append(cur_ear)
        MAR_buf.append(cur_mar)

        # -----------------------------
        # MLP Prediction
        # -----------------------------
        if len(EAR_buf) == 15:
            input_data = pd.DataFrame([[np.mean(EAR_buf), np.mean(MAR_buf)]],
                                      columns=['EAR', 'MAR'])
            feat_scaled = scaler.transform(input_data)
            pred = mlp.predict(feat_scaled)[0]
            drowsy_state = le.classes_[pred].upper()

            # Alarm Logic
            if drowsy_state in ["MICROSLEEP", "YAWNING"] or head_state in ["LOOKING RIGHT", "LOOKING LEFT","LOOKING DOWN","LOOKING UP"] :
                if alert_sound and not pygame.mixer.get_busy():
                    alert_sound.play()

    # -----------------------------
    # Dashboard UI
    # -----------------------------
    dashboard = np.zeros((h, 300, 3), dtype=np.uint8)

    cv2.putText(dashboard, "DRIVER ANALYTICS", (20, 40),
                cv2.FONT_HERSHEY_DUPLEX, 0.6, (255,255,255), 1)
    cv2.line(dashboard, (20,50), (280,50), (150,150,150), 1)

    y_offset = 90
    metrics = [
        (f"STATE: {drowsy_state}", (0,255,255)),
        (f"POSE : {head_state}", head_color),
        (f"EAR  : {cur_ear:.3f}", (200,200,200)),
        (f"MAR  : {cur_mar:.3f}", (200,200,200))
    ]

    for text, color in metrics:
        cv2.putText(dashboard, text, (20,y_offset),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)
        y_offset += 35

    if drowsy_state in ["MICROSLEEP", "YAWNING"] or head_state in ["LOOKING RIGHT", "LOOKING LEFT","LOOKING DOWN","LOOKING UP"] :
        cv2.rectangle(dashboard, (15, y_offset+10),
                      (285, y_offset+50), (0,0,255), -1)
        cv2.putText(dashboard, "ALARM ACTIVE",
                    (75, y_offset+37),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2)

    combined_view = np.hstack((frame, dashboard))
    cv2.imshow("Driver Monitoring System", combined_view)

    key = cv2.waitKey(1)
    if key == 27:
        break
    elif key == ord('s'):
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"report_{timestamp}.png"
        cv2.imwrite(filename, combined_view)
        print(f"Screenshot saved: {filename}")

cap.release()
cv2.destroyAllWindows()
pygame.mixer.quit()
