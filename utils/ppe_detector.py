"""
=========================================================
File Name : ppe_detector.py
Project   : Smart Safety Monitor
Author    : Vikas Mishra

Purpose
-------
Handle PPE model loading and PPE object filtering.

Responsibilities
----------------
1. Load PPE YOLO model.
2. Detect PPE objects.
3. Filter helmet detections.
4. Filter no-helmet detections.
5. Filter safety vest detections.
=========================================================
"""

from ultralytics import YOLO

from utils.constants import (
    PPE_MODEL_NAME,
    PPE_CONFIDENCE,
)


class PPEDetector:
    """
    Handles PPE model loading and object detection.
    """

    def __init__(self):

        print("=" * 55)
        print("Loading PPE model...")
        print("=" * 55)

        self.model = YOLO(PPE_MODEL_NAME)

        print("PPE model loaded successfully.\n")

    def detect(self, frame):
        """
        Detect PPE objects in a frame.
        """

        results = self.model.predict(
            source=frame,
            conf=PPE_CONFIDENCE,
            verbose=False
        )

        detections = []

        result = results[0]

        for box in result.boxes:

            class_id = int(box.cls[0])

            class_name = self.model.names[class_id]

            confidence = float(box.conf[0])

            x1, y1, x2, y2 = map(int, box.xyxy[0])

            detections.append(
                {
                    "class_id": class_id,
                    "class_name": class_name,
                    "confidence": confidence,
                    "bbox": (x1, y1, x2, y2),
                }
            )

        return detections


def get_helmet_detections(detections):
    """
    Return helmet detections.
    """

    return [
        detection
        for detection in detections
        if detection["class_name"] == "head_helmet"
    ]


def get_nohelmet_detections(detections):
    """
    Return no-helmet detections.
    """

    return [
        detection
        for detection in detections
        if detection["class_name"] == "head_nohelmet"
    ]


def get_vest_detections(detections):
    """
    Return safety vest detections.
    """

    return [
        detection
        for detection in detections
        if detection["class_name"] == "vest"
    ]