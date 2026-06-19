"""
=========================================================
File Name : camera.py
Project   : Smart Safety Monitor
Author    : Vikas Mishra

Purpose:
---------
This module is responsible for handling all webcam
operations such as:

1. Opening the webcam
2. Reading video frames
3. Releasing the webcam safely

Keeping camera logic in a separate module makes the
project clean, modular, and easy to maintain.
=========================================================
"""

import cv2

from utils.constants import CAMERA_INDEX


def initialize_camera():
    """
    Initialize the webcam.

    Returns:
        cv2.VideoCapture:
            Opened camera object.

    Raises:
        RuntimeError:
            If the webcam cannot be opened.
    """

    # On Windows, CAP_DSHOW provides a more stable backend
    # and usually starts the webcam faster.
    camera = cv2.VideoCapture(CAMERA_INDEX, cv2.CAP_DSHOW)

    if not camera.isOpened():
        raise RuntimeError("Unable to open the webcam.")

    return camera


def release_camera(camera):
    """
    Release the webcam and close all OpenCV windows.

    Args:
        camera (cv2.VideoCapture):
            Opened webcam object.
    """

    if camera is not None:
        camera.release()

    cv2.destroyAllWindows()