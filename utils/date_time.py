"""
=========================================================
File Name : date_time.py
Project   : Smart Safety Monitor
Author    : Vikas Mishra

Purpose
-------
Provides the current system date and time.

Responsibilities
----------------
1. Get current date and time.
2. Return formatted string for display.
=========================================================
"""

from datetime import datetime


def get_current_datetime():
    """
    Return current date and time as a formatted string.

    Returns
    -------
    str
        Example:
        21-06-2026 10:45:18
    """

    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")