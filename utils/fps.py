"""
=========================================================
File Name : fps.py
Project   : Smart Safety Monitor
Author    : Vikas Mishra

Purpose
-------
Calculate and display real-time Frames Per Second (FPS).

Responsibilities
----------------
1. Calculate FPS.
2. Update FPS every second.
3. Return current FPS value.

Design Principle
----------------
This module is responsible only for FPS calculation.
It contains no detection or drawing logic.
=========================================================
"""

import time


class FPSCounter:
    """
    Calculates real-time Frames Per Second (FPS).
    """

    def __init__(self):
        """
        Initialize FPS variables.
        """

        # Time when FPS calculation started.
        self.start_time = time.time()

        # Number of processed frames.
        self.frame_count = 0

        # Current FPS value.
        self.fps = 0

    def update(self):
        """
        Update FPS calculation.

        Returns
        -------
        int
            Current FPS value.
        """

        self.frame_count += 1

        elapsed_time = time.time() - self.start_time

        # Update FPS once every second.
        if elapsed_time >= 1:

            self.fps = self.frame_count

            self.frame_count = 0
            self.start_time = time.time()

        return self.fps