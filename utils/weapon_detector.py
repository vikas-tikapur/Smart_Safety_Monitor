"""
=========================================================
File Name : weapon_detector.py
Project   : Smart Safety Monitor
Author    : Vikas Mishra

Purpose
-------
Handle all weapon detection operations.

Responsibilities
----------------
1. Load Weapon YOLO model.
2. Detect weapons in frames.
3. Return formatted detections.
4. Filter weapon detections.

Future Responsibilities
-----------------------
- Knife Detection
- Rifle Detection
- Weapon Classification
=========================================================
"""

from ultralytics import YOLO

from utils.constants import (
    WEAPON_MODEL_PATH,
    WEAPON_CONFIDENCE,
)


class WeaponDetector:
    """
    Handles Weapon YOLO model.
    """

    def __init__(self):

        print("=" * 55)
        print("Loading Weapon model...")
        print("=" * 55)

        self.model = YOLO(WEAPON_MODEL_PATH)

        print("Weapon model loaded successfully.\n")

    def detect(self, frame):
        """
        Detect weapons in a frame.
        """

        results = self.model.predict(
            frame,
            conf=WEAPON_CONFIDENCE,
            verbose=False
        )

        detections = []

        for result in results:

            for box in result.boxes:

                class_id = int(box.cls[0])

                detections.append({

                    "class_name": self.model.names[class_id],

                    "confidence": float(box.conf[0]),

                    "bbox": list(
                        map(
                            int,
                            box.xyxy[0]
                        )
                    )

                })

        return detections


def get_weapon_detections(detections):
    """
    Return only weapon detections.
    """

    weapon_detections = []

    for detection in detections:

        if detection["class_name"] == "guns":

            weapon_detections.append(detection)

    return weapon_detections