"""
=========================================================
File Name : constants.py
Project   : Smart Safety Monitor
Author    : Vikas Mishra

Purpose:
---------
This file stores all project-wide constant values.
Keeping constants in one place makes the project
easy to maintain and modify.

Whenever a value needs to change, update it here
instead of searching through the entire project.
=========================================================
"""

# =========================================================
# Camera Settings
# =========================================================

# Default webcam index.
# 0 = Laptop/Internal webcam
# 1 = External USB webcam (if connected)
CAMERA_INDEX = 0


# =========================================================
# Display Window Settings
# =========================================================

# Window title shown when the camera starts.
WINDOW_NAME = "Smart Safety Monitor"

# =========================================================
# YOLO Model Settings
# =========================================================

# Name of the default YOLOv8 model.
YOLO_MODEL_NAME = "yolov8n.pt"


# =========================================================
# Detection Settings
# =========================================================

# Default confidence threshold.
# Objects below this confidence will be ignored.
YOLO_CONFIDENCE = 0.50