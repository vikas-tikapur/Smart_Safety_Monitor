"""
=========================================================
File Name : event_manager.py
Project   : Smart Safety Monitor
Author    : Vikas Mishra

Purpose
-------
Handle safety events.

Responsibilities
----------------
1. Save screenshots.
2. Log events.
3. Print event messages.

Future Responsibilities
-----------------------
- Email alerts
- Sound alerts
- Telegram alerts
- Dashboard notifications
=========================================================
"""

class EventManager:
    """
    Handles safety events.
    """

    def __init__(
        self,
        screenshot_manager,
        logger
    ):

        self.screenshot_manager = screenshot_manager
        self.logger = logger

    def handle_event(
        self,
        frame,
        event_name,
        person_count,
        mobile_count,
        helmet_count,
        nohelmet_count,
        vest_count
    ):
        """
        Handle a safety event.

        Parameters
        ----------
        frame : numpy.ndarray
            Current video frame.

        event_name : str
            Event name.

        person_count : int
            Number of detected persons.

        mobile_count : int
            Number of detected mobile phones.

        helmet_count : int
            Number of detected helmets.

        nohelmet_count : int
            Number of detected no-helmet detections.

        vest_count : int
            Number of detected safety vests.
        """

        # Save screenshot
        screenshot_name = self.screenshot_manager.save_screenshot(
            frame,
            event_name=event_name.lower().replace(" ", "_")
        )

        # Log event
        self.logger.log_event(
            event_name=event_name,
            person_count=person_count,
            mobile_count=mobile_count,
            helmet_count=helmet_count,
            nohelmet_count=nohelmet_count,
            vest_count=vest_count,
            screenshot_name=screenshot_name
        )

        print(f"{event_name} event handled successfully.")