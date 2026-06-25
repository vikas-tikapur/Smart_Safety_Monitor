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
3. Detect persons, mobile phones, and PPE.
4. Draw object detection results.
5. Display live counters.
6. Exit safely when 'Q' is pressed.
=========================================================
"""

import cv2

from utils.camera import initialize_camera, release_camera
from utils.constants import (
    WINDOW_NAME,
    MOBILE_FRAME_THRESHOLD,
    NOHELMET_FRAME_THRESHOLD,
)
from utils.detector import ObjectDetector
from utils.ppe_detector import (
    PPEDetector,
    get_helmet_detections,
    get_nohelmet_detections,
    get_vest_detections,
)
from utils.drawing import (
    draw_detection,
    draw_ppe_detection,
    draw_status_panel,
)
from utils.mobile_detector import get_mobile_detections
from utils.screenshot import ScreenshotManager
from utils.date_time import get_current_datetime
from utils.logger import EventLogger
from utils.violation_manager import ViolationManager
from utils.fps import FPSCounter


def main():
    """
    Start the Smart Safety Monitor application.
    """

    camera = None
    detector = None
    ppe_detector = None
    screenshot_manager = None
    logger = None
    fps_counter = FPSCounter()
    violation_manager = ViolationManager()

    # Frame-based event tracking
    mobile_frame_count = 0
    nohelmet_frame_count = 0

    print("=" * 55)
    print("        Smart Safety Monitor")
    print("=" * 55)
    print("Initializing application...\n")

    try:
        # Initialize webcam
        camera = initialize_camera()
        print("Webcam initialized successfully.")

        # Load YOLO model
        detector = ObjectDetector()
        print("YOLO model initialized successfully.\n")

        # Load PPE model
        ppe_detector = PPEDetector()
        print("PPE model initialized successfully.\n")

        # Initialize screenshot manager
        screenshot_manager = ScreenshotManager()
        print("Screenshot manager initialized successfully.\n")

        # Initialize event logger
        logger = EventLogger()
        print("Event logger initialized successfully.\n")

        print("Press 'Q' to exit.\n")

        while True:

            # Read current frame
            success, frame = camera.read()

            if not success:
                print("Error: Unable to capture frame.")
                break

            # Run YOLO detection
            detections = detector.detect(frame)

            # Run PPE detection
            ppe_detections = ppe_detector.detect(frame)
            helmet_detections = get_helmet_detections(ppe_detections)

            nohelmet_detections = get_nohelmet_detections(
                ppe_detections
            )

            vest_detections = get_vest_detections(
                ppe_detections
            )

            helmet_count = len(helmet_detections)
            nohelmet_count = len(nohelmet_detections)
            vest_count = len(vest_detections)

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
            # Draw Helmet Detections
            # ----------------------------------------
            for detection in helmet_detections:

                draw_ppe_detection(
                    frame,
                    detection,
                    color=(255, 0, 0)
                )

            # ----------------------------------------
            # Draw No Helmet Detections
            # ----------------------------------------
            for detection in nohelmet_detections:

                draw_ppe_detection(
                    frame,
                    detection,
                    color=(0, 0, 255)
                )

            # ----------------------------------------
            # Draw Vest Detections
            # ----------------------------------------
            for detection in vest_detections:

                draw_ppe_detection(
                    frame,
                    detection,
                    color=(255, 0, 255)
                )

            mobile_frame_count, mobile_violation = (
                violation_manager.check_mobile_violation(
                    mobile_count,
                    mobile_frame_count,
                    MOBILE_FRAME_THRESHOLD
                )
            )

            if mobile_violation:

                screenshot_name = screenshot_manager.save_screenshot(
                    frame,
                    event_name="mobile"
                )

                logger.log_event(
                    event_name="Mobile Detected",
                    person_count=person_count,
                    mobile_count=mobile_count,
                    helmet_count=helmet_count,
                    nohelmet_count=nohelmet_count,
                    vest_count=vest_count,
                    screenshot_name=screenshot_name
                )

                print("Mobile event confirmed. Screenshot captured.\n")

            nohelmet_frame_count, nohelmet_violation = (
                violation_manager.check_nohelmet_violation(
                    person_count,
                    nohelmet_count,
                    nohelmet_frame_count,
                    NOHELMET_FRAME_THRESHOLD
                )
            )

            if nohelmet_violation:

                screenshot_name = screenshot_manager.save_screenshot(
                    frame,
                    event_name="nohelmet"
                )

                logger.log_event(
                    event_name="No Helmet Detected",
                    person_count=person_count,
                    mobile_count=mobile_count,
                    helmet_count=helmet_count,
                    nohelmet_count=nohelmet_count,
                    vest_count=vest_count,
                    screenshot_name=screenshot_name
                )

                print("No Helmet violation detected.\n")

            # Calculate current FPS.
            fps = fps_counter.update()

            # Display FPS on the frame.
            # draw_fps(frame, fps)

            # Get current system date and time.
            current_time = get_current_datetime()

            # Draw status panel.
            draw_status_panel(
                frame,
                person_count,
                mobile_count,
                helmet_count,
                nohelmet_count,
                vest_count,
                fps,
                current_time
            )

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