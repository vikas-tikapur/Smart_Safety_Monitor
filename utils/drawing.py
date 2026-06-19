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
4. Display total detected person count.

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


def draw_detection(frame, x1, y1, x2, y2, label, color=(0, 255, 0)):
    """
    Draw a bounding box and label on the frame.

    Parameters
    ----------
    frame : numpy.ndarray
        Current webcam frame.

    x1, y1 : int
        Top-left corner.

    x2, y2 : int
        Bottom-right corner.

    label : str
        Label to display.

    color : tuple
        Bounding box color in BGR format.
    """

    # Draw bounding box
    cv2.rectangle(
        frame,
        (x1, y1),
        (x2, y2),
        color,
        2
    )

    # Draw label
    cv2.putText(
        frame,
        label,
        (x1, y1 - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        color,
        2
    )


def draw_person_count(frame, person_count):
    """
    Display total detected persons.
    """

    cv2.putText(
        frame,
        f"Person Count : {person_count}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.9,
        (0, 255, 255),
        2
    )


def draw_mobile_count(frame, mobile_count):
    """
    Display total detected mobile phones.
    """

    cv2.putText(
        frame,
        f"Mobile Count : {mobile_count}",
        (20, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.9,
        (255, 0, 0),
        2
    )