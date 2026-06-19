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

    # Draw a green rectangle around the detected object.
    cv2.rectangle(
        frame,
        (x1, y1),
        (x2, y2),
        (0, 255, 0),
        2
    )

    # Display the object label with confidence score.
    cv2.putText(
        frame,
        label,
        (x1, y1 - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (0, 255, 0),
        2
    )


def draw_person_count(frame, person_count):
    """
    Display the total number of detected persons.

    Parameters
    ----------
    frame : numpy.ndarray
        Current webcam frame.

    person_count : int
        Number of detected persons.
    """

    text = f"Person Count : {person_count}"

    # Display the person count at the top-left corner.
    cv2.putText(
        frame,
        text,
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.9,
        (0, 255, 255),
        2
    )