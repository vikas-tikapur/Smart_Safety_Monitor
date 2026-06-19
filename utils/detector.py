"""
=========================================================
File Name : detector.py
Project   : Smart Safety Monitor
Author    : Vikas Mishra

Purpose
-------
This module is responsible for all YOLO-related operations.

Responsibilities
----------------
1. Load the YOLO model.
2. Run object detection on frames.
3. Return detection results.

Future Responsibilities
-----------------------
- Person Detection
- Mobile Detection
- Helmet Detection
- Safety Vest Detection
- Weapon Detection
=========================================================
"""

from pathlib import Path

from ultralytics import YOLO

from utils.constants import YOLO_MODEL_NAME, YOLO_CONFIDENCE


class ObjectDetector:
    """
    Handles loading the YOLO model and performing object detection.
    """

    def __init__(self):
        """
        Initialize the detector and load the YOLO model.
        """

        # Project root directory
        self.project_root = Path(__file__).resolve().parent.parent

        # Models folder path
        self.models_folder = self.project_root / "models"

        # Create the models folder if it doesn't exist
        self.models_folder.mkdir(exist_ok=True)

        # Full model path
        self.model_path = self.models_folder / YOLO_MODEL_NAME

        # Load YOLO model
        self.model = self.load_model()

    def load_model(self):
        """
        Load the YOLO model.

        Returns
        -------
        ultralytics.YOLO
            Loaded YOLO model.
        """

        print("=" * 55)
        print("Loading YOLOv8 model...")
        print("=" * 55)

        # -------------------------------------------------
        # First Run
        # -------------------------------------------------
        #
        # If the model is not present inside the models
        # folder, Ultralytics automatically downloads it.
        #
        # After the first download, you can manually move
        # the downloaded file into the models folder.
        #
        # In a later milestone we'll automate that process.
        # -------------------------------------------------

        if self.model_path.exists():
            model = YOLO(str(self.model_path))
        else:
            print("Model not found inside models folder.")
            print("Downloading YOLOv8 model for the first time...\n")

            model = YOLO(YOLO_MODEL_NAME)

        print("YOLO model loaded successfully.\n")

        return model

    def detect(self, frame):
        """
        Run object detection on a single frame.

        Parameters
        ----------
        frame : numpy.ndarray
            Input image/frame.

        Returns
        -------
        list
            Detection results returned by YOLO.
        """

        results = self.model.predict(
            source=frame,
            conf=YOLO_CONFIDENCE,
            verbose=False
        )

        return results