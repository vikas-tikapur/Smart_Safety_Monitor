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

    def check_violation(
        self,
        event_active,
        object_count,
        frame_count,
        threshold
    ):
        """
        Generic violation checker.

        Parameters
        ----------
        event_active : bool
            Current event state.

        object_count : int
            Number of detected objects.

        frame_count : int
            Consecutive detection frame count.

        threshold : int
            Minimum consecutive frames required.

        Returns
        -------
        tuple
            (
                updated_frame_count,
                updated_event_state,
                violation_detected
            )
        """

        # Object disappeared
        if object_count == 0:

            return 0, False, False

        # Object detected
        frame_count += 1

        # Trigger event only once
        if (
            frame_count >= threshold
            and not event_active
        ):

            return frame_count, True, True

        return frame_count, event_active, False

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

        (
            frame_count,
            self.mobile_event_active,
            violation_detected
        ) = self.check_violation(
            event_active=self.mobile_event_active,
            object_count=mobile_count,
            frame_count=frame_count,
            threshold=threshold
        )

        return frame_count, violation_detected

    def check_nohelmet_violation(
        self,
        person_count,
        nohelmet_count,
        frame_count,
        threshold
    ):
        """
        Check whether a no-helmet violation should be triggered.
        """

        # No worker or no violation
        if person_count == 0 or nohelmet_count == 0:

            self.nohelmet_event_active = False

            return 0, False

        (
            frame_count,
            self.nohelmet_event_active,
            violation_detected
        ) = self.check_violation(
            event_active=self.nohelmet_event_active,
            object_count=nohelmet_count,
            frame_count=frame_count,
            threshold=threshold
        )

        return frame_count, violation_detected

    def check_novest_violation(
        self,
        person_count,
        vest_count,
        frame_count,
        threshold
    ):
        """
        Check whether a no-vest violation should be triggered.

        Parameters
        ----------
        person_count : int
            Number of detected persons.

        vest_count : int
            Number of detected safety vests.

        frame_count : int
            Consecutive violation frames.

        threshold : int
            Minimum consecutive frames required.
        """

        # No worker OR vest detected
        if person_count == 0 or vest_count > 0:

            self.novest_event_active = False

            return 0, False

        (
            frame_count,
            self.novest_event_active,
            violation_detected
        ) = self.check_violation(
            event_active=self.novest_event_active,
            object_count=person_count,
            frame_count=frame_count,
            threshold=threshold
        )

        return frame_count, violation_detected