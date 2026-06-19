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
3. Detect people in real-time.
4. Draw detection results.
5. Exit safely when 'Q' is pressed.
=========================================================
"""

import cv2

from utils.camera import initialize_camera, release_camera
from utils.constants import WINDOW_NAME
from utils.detector import ObjectDetector
from utils.drawing import draw_detection, draw_person_count


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
            # Store total detected persons in the current frame.
            person_count = 0

            if not success:
                print("Error: Unable to capture frame.")
                break

            # Run YOLO detection
            detections = detector.detect(frame)

            # Draw only PERSON detections
            for detection in detections:

                if detection["class_name"] != "person":
                    continue

                # Increment the detected person count.
                person_count += 1

                x1, y1, x2, y2 = detection["bbox"]
                confidence = detection["confidence"]

                label = f"Person {confidence:.2f}"

                draw_detection(
                    frame,
                    x1,
                    y1,
                    x2,
                    y2,
                    label
                )

                # Display total detected persons.
                draw_person_count(frame, person_count)

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