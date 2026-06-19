"""
=========================================================
File Name : drawing.py
Project   : Smart Safety Monitor
Author    : Vikas Mishra

Purpose
-------
This module is responsible for drawing detection
information on video frames.

Responsibilities
----------------
1. Draw bounding boxes.
2. Display class names.
3. Display confidence scores.

Future Responsibilities
-----------------------
- Different colors for different object classes.
- Warning messages.
- Safety alerts.
- Status indicators.

Design Principle
----------------
This module is responsible only for visualization.
No detection logic should be written here.
=========================================================
"""

import cv2


def draw_detection(frame, x1, y1, x2, y2, label):
    """
    Draw a bounding box and label on the frame.

    Parameters
    ----------
    frame : numpy.ndarray
        Current webcam frame.

    x1, y1 : int
        Top-left corner of the bounding box.

    x2, y2 : int
        Bottom-right corner of the bounding box.

    label : str
        Text displayed above the bounding box.
    """

    # Draw rectangle around detected object.
    cv2.rectangle(
        frame,
        (x1, y1),
        (x2, y2),
        (0, 255, 0),
        2
    )

    # Draw object label.
    cv2.putText(
        frame,
        label,
        (x1, y1 - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (0, 255, 0),
        2
    )