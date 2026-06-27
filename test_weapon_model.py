"""
=========================================================
File Name : test_weapon_model.py
Project   : Smart Safety Monitor
Author    : Vikas Mishra

Purpose
-------
Standalone testing for Weapon Detection Model.
=========================================================
"""

import cv2

from utils.weapon_detector import (
    WeaponDetector,
    get_weapon_detections
)
from utils.drawing import draw_ppe_detection


print("=" * 50)
print("Loading Weapon Model...")
print("=" * 50)

weapon_detector = WeaponDetector()

print("Opening Camera Source...\n")

camera = cv2.VideoCapture("videos/gun_test.mp4")

while True:

    success, frame = camera.read()

    if not success:
        break

    detections = weapon_detector.detect(frame)

    weapon_detections = get_weapon_detections(detections)

    for detection in weapon_detections:

        draw_ppe_detection(
            frame,
            detection,
            color=(0, 165, 255)   # Orange
        )

    cv2.imshow("Weapon Model Validation", frame)

    key = cv2.waitKey(1) & 0xFF

    if key in (ord("q"), ord("Q")):
        break

camera.release()

cv2.destroyAllWindows()

print("\nTesting Finished.")