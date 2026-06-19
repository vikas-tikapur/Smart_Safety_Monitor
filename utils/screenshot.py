"""
=========================================================
File Name : screenshot.py
Project   : Smart Safety Monitor
Author    : Vikas Mishra

Purpose
-------
This module handles screenshot capturing.

Responsibilities
----------------
1. Create screenshots directory (if needed).
2. Generate unique filename.
3. Save screenshot.
4. Return saved screenshot path.

Future Responsibilities
-----------------------
- Save screenshots based on event type.
- Store screenshots in event-wise folders.
- Compress screenshots (optional).
=========================================================
"""

from pathlib import Path
from datetime import datetime

import cv2


class ScreenshotManager:
    """
    Handles saving screenshots captured from the webcam.
    """

    def __init__(self):
        """
        Initialize the screenshot manager.
        """

        # Project root directory
        self.project_root = Path(__file__).resolve().parent.parent

        # Screenshot directory
        self.screenshot_folder = self.project_root / "screenshots"

        # Create folder if it doesn't exist
        self.screenshot_folder.mkdir(exist_ok=True)

    def save_screenshot(self, frame, event_name="event"):
        """
        Save the current frame as an image.

        Parameters
        ----------
        frame : numpy.ndarray
            Current webcam frame.

        event_name : str
            Name of the event.
            Example:
                mobile
                weapon
                helmet

        Returns
        -------
        str
            Saved screenshot path.
        """

        # Generate timestamp
        # Include microseconds to ensure every filename is unique.
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")

        # Example:
        # mobile_2026-06-19_19-15-30.jpg
        filename = f"{event_name}_{timestamp}.jpg"

        # Full image path
        image_path = self.screenshot_folder / filename

        # Save image
        cv2.imwrite(str(image_path), frame)

        print(f"Screenshot saved : {filename}")

        return str(image_path)