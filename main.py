"""
=========================================================
Project   : Smart Safety Monitor
File Name : main.py
Author    : Vikas Mishra

Purpose
-------
Main entry point of the application.

Responsibilities
----------------
1. Initialize the webcam.
2. Initialize the YOLO detector.
3. Detect persons and mobile phones.
4. Draw detection results.
5. Display live counters.
6. Exit safely when 'Q' is pressed.
=========================================================
"""

import cv2

from utils.camera import initialize_camera, release_camera
from utils.constants import WINDOW_NAME
from utils.detector import ObjectDetector
from utils.drawing import (
    draw_detection,
    draw_person_count,
    draw_mobile_count,
)
from utils.mobile_detector import get_mobile_detections


def main():
    """
    Start the Smart Safety Monitor application.
    """

    camera = None
    detector = None

    print("=" * 55)
    print("        Smart Safety Monitor")
    print("=" * 55)
    print("Initializing application...\n")

    try:
        # Initialize webcam
        camera = initialize_camera()
        print("✓ Webcam initialized successfully.")

        # Load YOLO model
        detector = ObjectDetector()
        print("✓ YOLO model initialized successfully.\n")

        print("Press 'Q' to exit.\n")

        while True:

            # Read current frame
            success, frame = camera.read()

            if not success:
                print("Error: Unable to capture frame.")
                break

            # Run YOLO detection
            detections = detector.detect(frame)

            # Get only mobile detections
            mobile_detections = get_mobile_detections(detections)

            # Frame-wise counters
            person_count = 0
            mobile_count = len(mobile_detections)

            # ----------------------------------------
            # Draw Person Detections
            # ----------------------------------------
            for detection in detections:

                if detection["class_name"] != "person":
                    continue

                person_count += 1

                x1, y1, x2, y2 = detection["bbox"]

                label = f"Person {detection['confidence']:.2f}"

                draw_detection(
                    frame,
                    x1,
                    y1,
                    x2,
                    y2,
                    label,
                    color=(0, 255, 0)
                )

            # ----------------------------------------
            # Draw Mobile Detections
            # ----------------------------------------
            for detection in mobile_detections:

                x1, y1, x2, y2 = detection["bbox"]

                label = f"Mobile {detection['confidence']:.2f}"

                draw_detection(
                    frame,
                    x1,
                    y1,
                    x2,
                    y2,
                    label,
                    color=(255, 0, 0)
                )

            # ----------------------------------------
            # Draw Counters
            # ----------------------------------------
            draw_person_count(frame, person_count)
            draw_mobile_count(frame, mobile_count)

            # Display frame
            cv2.imshow(WINDOW_NAME, frame)

            # Exit on Q
            key = cv2.waitKey(1) & 0xFF

            if key in (ord("q"), ord("Q")):
                print("\nExit command received.")
                break

    except Exception as error:
        print(f"\nApplication Error: {error}")

    finally:
        release_camera(camera)

        print("Webcam released successfully.")
        print("Application closed successfully.")


if __name__ == "__main__":
    main()