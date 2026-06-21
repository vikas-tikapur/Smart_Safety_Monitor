"""
=========================================================
File Name : analytics.py
Project   : Smart Safety Monitor
Author    : Vikas Mishra

Purpose
-------
Read detection logs and calculate dashboard statistics.

Responsibilities
----------------
1. Read detections.csv
2. Calculate total events
3. Calculate total mobile events
4. Return dashboard statistics
=========================================================
"""

from pathlib import Path
import pandas as pd


class DashboardAnalytics:
    """
    Reads detection logs and prepares statistics
    for the dashboard.
    """

    # Default statistics returned when no log data is available.
    empty_stats = {
        "total_events": 0,
        "today_events": 0,
        "mobile_events": 0,
        "total_persons": 0,
        "latest_event": "No Data",
        "last_screenshot": "No Screenshot"
    }

    def __init__(self):

        # Project root directory
        self.project_root = Path(__file__).resolve().parent.parent

        # CSV file path
        self.csv_file = self.project_root / "logs" / "detections.csv"

    def get_statistics(self):
        """
        Returns dashboard statistics.

        Returns
        -------
        dict
        """

        # No CSV file available
        if not self.csv_file.exists():

            return self.empty_stats

        df = pd.read_csv(self.csv_file)

        # Empty CSV
        if df.empty:

            return self.empty_stats

        # Convert timestamp to datetime
        df["Timestamp"] = pd.to_datetime(df["Timestamp"])

        # Get today's date
        today = pd.Timestamp.now().date()

        # Count today's events
        today_events = len(df[df["Timestamp"].dt.date == today])

        stats = {
            "total_events": len(df),

            "today_events": today_events,

            "mobile_events": len(
                df[df["Event"] == "Mobile Detected"]
            ),

            "total_persons": int(df["Person Count"].sum()),

            "latest_event": df.iloc[-1]["Event"],

            "last_screenshot": df.iloc[-1]["Screenshot"]
        }

        return stats