"""
=========================================================
File Name : violation_manager.py
Project   : Smart Safety Monitor
Author    : Vikas Mishra

Purpose
-------
Manage workplace safety violations.

Responsibilities
----------------
1. Detect mobile violations.
2. Detect PPE violations.
3. Prevent duplicate events.
4. Prepare violation data for logging.

Future Responsibilities
-----------------------
- Weapon violations
- Fire detection
- Restricted area violations
- Intrusion detection
=========================================================
"""


class ViolationManager:
    """
    Handles workplace safety violations.
    """

    def __init__(self):
        """
        Initialize violation manager.
        """

        # Mobile violation state
        self.mobile_event_active = False

        # PPE violation state
        self.nohelmet_event_active = False
        self.novest_event_active = False

        # Future violation states
        self.weapon_event_active = False
        self.fire_event_active = False

    def check_mobile_violation(
        self,
        mobile_count,
        frame_count,
        threshold
    ):
        """
        Check whether a mobile violation should be triggered.

        Parameters
        ----------
        mobile_count : int
            Number of detected mobile phones.

        frame_count : int
            Consecutive frames containing a mobile phone.

        threshold : int
            Minimum consecutive frames required.

        Returns
        -------
        tuple
            (
                updated_frame_count,
                violation_detected
            )
        """

        # No mobile detected
        if mobile_count == 0:

            self.mobile_event_active = False

            return 0, False

        # Mobile detected
        frame_count += 1

        # Trigger only once
        if (
            frame_count >= threshold
            and not self.mobile_event_active
        ):

            self.mobile_event_active = True

            return frame_count, True

        return frame_count, False