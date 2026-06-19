"""
=========================================================
File Name : mobile_detector.py
Project   : Smart Safety Monitor
Author    : Vikas Mishra

Purpose
-------
This module contains all logic related to mobile
phone detection.

Responsibilities
----------------
1. Filter only mobile phone detections.
2. Apply mobile confidence threshold.
3. Return filtered mobile detections.

Future Responsibilities
-----------------------
- Frame confirmation logic.
- Screenshot trigger.
- CSV logging.
=========================================================
"""

from utils.constants import MOBILE_CONFIDENCE


def get_mobile_detections(detections):
    """
    Filter only valid mobile phone detections.

    Parameters
    ----------
    detections : list
        List of detected objects returned by detector.py.

    Returns
    -------
    list
        Filtered mobile phone detections.
    """

    mobile_detections = []

    for detection in detections:

        # Ignore non-mobile objects.
        if detection["class_name"] != "cell phone":
            continue

        # Ignore low-confidence detections.
        if detection["confidence"] < MOBILE_CONFIDENCE:
            continue

        mobile_detections.append(detection)

    return mobile_detections