"""
=========================================================
File Name : logger.py
Project   : Smart Safety Monitor
Author    : Vikas Mishra

Purpose
-------
This module handles CSV event logging.

Responsibilities
----------------
1. Create logs directory.
2. Create detections.csv file.
3. Write CSV header (first run only).
4. Append detection events.

Future Responsibilities
-----------------------
- Store additional object information.
- Store event severity.
- Store alert status.
=========================================================
"""

from pathlib import Path
import csv
from datetime import datetime


class EventLogger:
    """
    Handles writing detection events to a CSV file.
    """

    def __init__(self):
        """
        Initialize the logger.
        """

        print("Creating logger...")

        # Project root directory
        self.project_root = Path(__file__).resolve().parent.parent

        # Logs directory
        self.logs_folder = self.project_root / "logs"
        self.logs_folder.mkdir(exist_ok=True)

        # CSV file
        self.csv_file = self.logs_folder / "detections.csv"

        print("CSV exists:", self.csv_file.exists())
        print("CSV path:", self.csv_file)

        # Create CSV with header if it doesn't exist
        if not self.csv_file.exists():

            with open(self.csv_file, "w", newline="", encoding="utf-8") as file:

                writer = csv.writer(file)

                writer.writerow([
                    "Timestamp",
                    "Event",
                    "Person Count",
                    "Mobile Count",
                    "Helmet Count",
                    "No Helmet Count",
                    "Vest Count",
                    "Screenshot"
                ])

            print("CSV header written.")

    def log_event(
        self,
        event_name,
        person_count,
        mobile_count,
        helmet_count,
        nohelmet_count,
        vest_count,
        screenshot_name
    ):
        """
        Append a detection event to the CSV file.
        """

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(self.csv_file, "a", newline="", encoding="utf-8") as file:

            writer = csv.writer(file)

            writer.writerow([
                timestamp,
                event_name,
                person_count,
                mobile_count,
                helmet_count,
                nohelmet_count,
                vest_count,
                screenshot_name
            ])

        print("Event logged successfully.")