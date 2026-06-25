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

# =========================================================
# Mobile Phone Detection Settings
# =========================================================

# Minimum confidence required for mobile phone detection.
# Lower values increase detections but also increase false positives.
# Higher values reduce false positives but may miss some phones.
MOBILE_CONFIDENCE = 0.60

# Number of consecutive frames required before confirming
# that a mobile phone is actually detected.
# (Will be used in a later milestone.)
MOBILE_FRAME_THRESHOLD = 5

# Number of consecutive frames required before confirming
# that a no-helmet violation is actually detected.
NOHELMET_FRAME_THRESHOLD = 5

# Number of consecutive frames required before confirming
# that a no-vest violation is actually detected.
NOVEST_FRAME_THRESHOLD = 5

# =========================================================
# PPE Detection Settings
# =========================================================

# Path to the PPE model.
PPE_MODEL_NAME = "models/ppe/best.pt"

# Confidence threshold for PPE detection.
# Objects below this confidence will be ignored.
PPE_CONFIDENCE = 0.35