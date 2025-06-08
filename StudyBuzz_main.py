import cv2
import mediapipe as mp
import math
import threading
import pyttsx3
import os
import time

# -------------------------- CONFIG --------------------------

EAR_THRESHOLD = 0.25        # Eye Aspect Ratio threshold
EYE_CLOSED_FRAMES = 60      # Number of frames to consider as sleeping
MAR_THRESHOLD = 0.03        # Mouth Aspect Ratio threshold for yawning
ALERT_COOLDOWN = 5          # Minimum seconds between spoken alerts

# -------------------------- TTS ALERT SETUP --------------------------

engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

# Use threading so speech doesn't block the main loop
def speak_alert(message):
    def speak():
        engine.say(message)
        engine.runAndWait()
    threading.Thread(target=speak).start()

# -------------------------- MEDIAPIPE SETUP --------------------------

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(
    static_image_mode=False,
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

# Eye and mouth landmark indices
LEFT_EYE = [362, 385, 387, 263, 373, 380]
RIGHT_EYE = [33, 160, 158, 133, 153, 144]
MOUTH = [13, 14]

# -------------------------- UTILITIES --------------------------

def distance(p1, p2):
    return math.hypot(p2[0] - p1[0], p2[1] - p1[1])

# -------------------------- MAIN LOOP --------------------------

cap = cv2.VideoCapture(0)
eye_closed_time = 0
last_eye_alert_time = 0
last_yawn_alert_time = 0

print("StudyBuzz is running. Press 'q' to quit.")

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        h, w, _ = frame.shape
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(rgb)
        current_time = time.time()

        if results.multi_face_landmarks:
            face = results.multi_face_landmarks[0]
            landmarks = face.landmark

            def get_coords(points):
                return [(int(landmarks[p].x * w), int(landmarks[p].y * h)) for p in points]

            left_eye = get_coords(LEFT_EYE)
            right_eye = get_coords(RIGHT_EYE)
            mouth = get_coords(MOUTH)

            def get_ear(eye):
                v1 = distance(eye[1], eye[5])
                v2 = distance(eye[2], eye[4])
                h1 = distance(eye[0], eye[3])
                return (v1 + v2) / (2.0 * h1)

            left_ear = get_ear(left_eye)
            right_ear = get_ear(right_eye)
            ear = (left_ear + right_ear) / 2.0

            mouth_open = distance(mouth[0], mouth[1])
            mar = mouth_open / w

            # Debug display
            cv2.putText(frame, f"EAR: {ear:.2f}", (30, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            cv2.putText(frame, f"MAR: {mar:.3f}", (30, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)

            # Eye closure detection
            if ear < EAR_THRESHOLD:
                eye_closed_time += 1
                if eye_closed_time > EYE_CLOSED_FRAMES:
                    cv2.putText(frame, "EYES CLOSED! WAKE UP!", (30, 120), cv2.FONT_HERSHEY_SIMPLEX,
                                1.2, (0, 0, 255), 3)
                    if current_time - last_eye_alert_time > ALERT_COOLDOWN:
                        speak_alert("Eyes closed! Wake up!")
                        last_eye_alert_time = current_time
            else:
                eye_closed_time = 0

            # Yawning detection
            if mar > MAR_THRESHOLD:
                cv2.putText(frame, "YAWNING... Stay awake!", (30, 160), cv2.FONT_HERSHEY_SIMPLEX,
                            0.9, (255, 0, 0), 2)
                if current_time - last_yawn_alert_time > ALERT_COOLDOWN:
                    speak_alert("You are yawning. Stay awake!")
                    last_yawn_alert_time = current_time

        # Show the frame
        cv2.imshow("StudyBuzz", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    cap.release()
    cv2.destroyAllWindows()
