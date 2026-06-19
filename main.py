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
3. Display live webcam frames.
4. Exit safely when 'Q' is pressed.

Note:
-----
In this milestone, the YOLO model is only loaded.
Object detection will be added in the next milestone.
=========================================================
"""

import cv2

from utils.camera import initialize_camera, release_camera
from utils.constants import WINDOW_NAME
from utils.detector import ObjectDetector


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
        # -----------------------------------------
        # Step 1 : Initialize Webcam
        # -----------------------------------------
        camera = initialize_camera()
        print("Webcam initialized successfully.")

        # -----------------------------------------
        # Step 2 : Load YOLO Model
        # -----------------------------------------
        detector = ObjectDetector()
        print("YOLO model initialized successfully.\n")

        print("Press 'Q' to exit.\n")

        while True:

            # Read one frame from webcam
            success, frame = camera.read()

            if not success:
                print("Error: Unable to capture frame.")
                break

            # -------------------------------------------------
            # Detection will be added in the next milestone.
            #
            # results = detector.detect(frame)
            # -------------------------------------------------

            cv2.imshow(WINDOW_NAME, frame)

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