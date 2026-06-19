"""
=========================================================
Project   : Smart Safety Monitor
File Name : main.py
Author    : Vikas Mishra

Purpose:
---------
This is the main entry point of the application.

Responsibilities:
1. Initialize the webcam.
2. Read live video frames.
3. Display the webcam feed.
4. Handle user input.
5. Release resources safely before exiting.
=========================================================
"""

import cv2

from utils.camera import initialize_camera, release_camera
from utils.constants import WINDOW_NAME


def main():
    """
    Start the Smart Safety Monitor application.
    """

    # Initialize camera variable.
    # This prevents errors in the finally block if camera initialization fails.
    camera = None

    print("=" * 55)
    print("        Smart Safety Monitor")
    print("=" * 55)
    print("Initializing application...\n")

    try:
        # Initialize the webcam.
        camera = initialize_camera()

        print("Webcam initialized successfully.")
        print("Press 'Q' to exit the application.\n")

        while True:
            # Read one frame from the webcam.
            success, frame = camera.read()

            # Stop execution if the frame cannot be captured.
            if not success:
                print("Error: Unable to read frame from webcam.")
                break

            # Display the current frame.
            cv2.imshow(WINDOW_NAME, frame)

            # Wait for keyboard input.
            key = cv2.waitKey(1) & 0xFF

            # Exit when 'Q' or 'q' is pressed.
            if key in (ord("q"), ord("Q")):
                print("\nExit command received.")
                break

    except Exception as error:
        print(f"\nApplication Error: {error}")

    finally:
        # Always release the camera.
        release_camera(camera)

        print("Webcam released successfully.")
        print("Application closed successfully.")


if __name__ == "__main__":
    main()