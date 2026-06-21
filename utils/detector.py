"""
=========================================================
File Name : detector.py
Project   : Smart Safety Monitor
Author    : Vikas Mishra

Purpose
-------
This module handles all YOLO-related operations.

Responsibilities
----------------
1. Load the YOLO model.
2. Run YOLO inference on the input frame.
3. Return clean detection data.

Future Responsibilities
-----------------------
- Person Detection
- Mobile Detection
- Helmet Detection
- Safety Vest Detection
- Weapon Detection
=========================================================
"""

from ultralytics import YOLO

from utils.constants import YOLO_CONFIDENCE, YOLO_MODEL_NAME


class ObjectDetector:
    """
    Handles YOLO model loading and object detection.
    """

    # Load the YOLO model only once during application startup.
    def __init__(self):
        """Load the YOLO model once."""

        print("=" * 55)
        print("Loading YOLOv8 model...")
        print("=" * 55)

        self.model = YOLO(YOLO_MODEL_NAME)

        print("YOLO model loaded successfully.\n")

    def detect(self, frame):
        """
        Detect objects in a single frame.

        Parameters
        ----------
        frame : numpy.ndarray
            Current webcam frame.

        Returns
        -------
        list
            List of processed detections.
        """

        results = self.model.predict(
            source=frame,
            conf=YOLO_CONFIDENCE,
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