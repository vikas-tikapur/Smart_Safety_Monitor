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


def draw_ppe_detection(frame, detection, color):
    """
    Draw a PPE detection bounding box and label.

    Parameters
    ----------
    frame : numpy.ndarray
        Current webcam frame.

    detection : dict
        PPE detection dictionary.

    color : tuple
        Bounding box color in BGR format.
    """

    x1, y1, x2, y2 = detection["bbox"]

    label = (
        f"{detection['class_name']} "
        f"{detection['confidence']:.2f}"
    )

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


def draw_status_panel(
    frame,
    person_count,
    mobile_count,
    helmet_count,
    nohelmet_count,
    vest_count,
    weapon_count,
    fps,
    current_time
):
    """
    Draw a professional status panel on the frame.

    Parameters
    ----------
    frame : numpy.ndarray
        Current video frame.

    person_count : int
        Total detected persons.

    mobile_count : int
        Total detected mobile phones.

    helmet_count : int
        Total detected helmets.

    nohelmet_count : int
        Total detected no-helmet instances.

    vest_count : int
        Total detected vests.

    fps : int
        Current frames per second.
    """

    # Panel position
    x = 10
    y = 10
    width = 310
    height = 270

    # Black filled rectangle
    cv2.rectangle(
        frame,
        (x, y),
        (x + width, y + height),
        (40, 40, 40),
        -1
    )

    # White border
    cv2.rectangle(
        frame,
        (x, y),
        (x + width, y + height),
        (255, 255, 255),
        2
    )

    # Title
    cv2.putText(
        frame,
        "SMART SAFETY MONITOR",
        (20, 35),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.60,
        (0, 255, 255),
        2
    )

    cv2.line(
        frame,
        (20, 45),
        (300, 45),
        (180, 180, 180),
        1
    )

    # Person count
    cv2.putText(
        frame,
        f"Persons      : {person_count}",
        (20, 65),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.55,
        (255, 255, 255),
        2
    )

    # Mobile count
    cv2.putText(
        frame,
        f"Mobile       : {mobile_count}",
        (20, 90),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.55,
        (255, 255, 255),
        2
    )

    # Helmet count
    cv2.putText(
        frame,
        f"Helmet       : {helmet_count}",
        (20, 115),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.55,
        (255, 0, 0),
        2
    )

    # No Helmet count
    cv2.putText(
        frame,
        f"No Helmet    : {nohelmet_count}",
        (20, 140),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.55,
        (0, 0, 255),
        2
    )

    # Vest count
    cv2.putText(
        frame,
        f"Vest         : {vest_count}",
        (20, 165),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.55,
        (255, 0, 255),
        2
    )

    # Weapon count
    cv2.putText(
        frame,
        f"Weapons      : {weapon_count}",
        (20, 190),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.55,
        (255, 255, 255),
        2
    )

    cv2.line(
        frame,
        (20, 205),
        (300, 205),
        (180, 180, 180),
        1
    )

    # FPS
    cv2.putText(
        frame,
        f"FPS          : {fps}",
        (20, 230),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.55,
        (255, 255, 255),
        2
    )

    cv2.putText(
        frame,
        "Status       : Monitoring",
        (20, 253),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.55,
        (0, 255, 0),
        2
    )

    cv2.putText(
        frame,
        f"Time : {current_time}",
        (20, 273),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.48,
        (255, 255, 255),
        1
    )