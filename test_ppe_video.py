"""
=========================================================
File Name : test_ppe_video.py
Project   : Smart Safety Monitor

Purpose
-------
Validate the PPE YOLO model using a recorded video.

This file is only for testing the PPE model.
It does not affect the main application.
=========================================================
"""

import cv2
from ultralytics import YOLO

# -------------------------------------------------
# Configuration
# -------------------------------------------------

VIDEO_PATH = "videos/helmet_safety_vest.mp4"
MODEL_PATH = "models/ppe/best.pt"
CONFIDENCE = 0.35

# -------------------------------------------------
# Load Model
# -------------------------------------------------

print("=" * 50)
print("Loading PPE Model...")
print("=" * 50)

model = YOLO(MODEL_PATH)

print("Model Loaded Successfully.\n")

# -------------------------------------------------
# Open Video
# -------------------------------------------------

cap = cv2.VideoCapture(VIDEO_PATH)

if not cap.isOpened():
    raise RuntimeError("Unable to open video.")

print("Video Loaded Successfully.\n")

# -------------------------------------------------
# Process Video
# -------------------------------------------------

while True:

    success, frame = cap.read()

    if not success:
        break

    results = model.predict(
        source=frame,
        conf=CONFIDENCE,
        verbose=False
    )

    annotated_frame = results[0].plot()

    cv2.imshow("PPE Model Validation", annotated_frame)

    key = cv2.waitKey(25) & 0xFF

    if key in (ord("q"), ord("Q")):
        break

cap.release()
cv2.destroyAllWindows()

print("\nTesting Finished.")