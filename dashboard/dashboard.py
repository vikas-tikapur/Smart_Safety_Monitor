"""
=========================================================
File Name : dashboard.py
Project   : Smart Safety Monitor
Author    : Vikas Mishra

Purpose
-------
Display dashboard statistics in a Tkinter window.

Responsibilities
----------------
1. Create dashboard window.
2. Read analytics data.
3. Display project statistics.
=========================================================
"""

import tkinter as tk

from dashboard.analytics import DashboardAnalytics


class Dashboard:
    """
    Displays Smart Safety Monitor dashboard.
    """

    def __init__(self):

        # Create analytics object
        self.analytics = DashboardAnalytics()

        # Load dashboard statistics
        self.load_statistics()

        # Create main window
        self.root = tk.Tk()

        self.root.title("Smart Safety Monitor Dashboard")
        self.root.geometry("700x500")
        self.root.resizable(False, False)

        # -----------------------------
        # Main Layout Frames
        # -----------------------------

        self.header_frame = tk.Frame(self.root)
        self.header_frame.pack(fill="x", pady=10)

        self.stats_frame = tk.Frame(self.root)
        self.stats_frame.pack(fill="both", expand=True, padx=15)

        self.info_frame = tk.Frame(self.root)
        self.info_frame.pack(fill="x", padx=15, pady=10)

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(fill="x", pady=10)

        # Store card value labels for future updates.
        self.card_labels = {}

        self.create_widgets()

    def load_statistics(self):
        """
        Load the latest dashboard statistics.
        """

        self.stats = self.analytics.get_statistics()

    def refresh_dashboard(self):
        """
        Refresh dashboard statistics automatically.
        """

        # Read latest statistics
        self.stats = self.analytics.get_statistics()

        # Update cards
        self.card_labels["Total Events"].config(
            text=str(self.stats["total_events"])
        )

        self.card_labels["Today's Events"].config(
            text=str(self.stats["today_events"])
        )

        self.card_labels["Mobile Events"].config(
            text=str(self.stats["mobile_events"])
        )

        self.card_labels["Total Persons"].config(
            text=str(self.stats["total_persons"])
        )

        # Update information panel
        self.event_label.config(
            text=f"Latest Event : {self.stats['latest_event']}"
        )

        self.screenshot_label.config(
            text=f"Last Screenshot : {self.stats['last_screenshot']}"
        )

        # Refresh every 2 seconds
        self.root.after(2000, self.refresh_dashboard)

    def create_widgets(self):
        """
        Create dashboard labels.
        """

        title = tk.Label(
            self.header_frame,
            text="SMART SAFETY DASHBOARD",
            font=("Arial", 16, "bold")
        )

        title.pack(pady=15)

        # -----------------------------
        # Statistics Cards
        # -----------------------------

        self.create_stat_card(
            self.stats_frame,
            "Total Events",
            self.stats["total_events"],
            0,
            0
        )

        self.create_stat_card(
            self.stats_frame,
            "Today's Events",
            self.stats["today_events"],
            0,
            1
        )

        self.create_stat_card(
            self.stats_frame,
            "Mobile Events",
            self.stats["mobile_events"],
            1,
            0
        )

        self.create_stat_card(
            self.stats_frame,
            "Total Persons",
            self.stats["total_persons"],
            1,
            1
        )

        self.stats_frame.columnconfigure(0, weight=1)
        self.stats_frame.columnconfigure(1, weight=1)

        self.stats_frame.rowconfigure(0, weight=1)
        self.stats_frame.rowconfigure(1, weight=1)

        # -----------------------------
        # Information Panel
        # -----------------------------

        self.event_label = tk.Label(
            self.info_frame,
            text=f"Latest Event : {self.stats['latest_event']}",
            anchor="w",
            font=("Arial", 11)
        )

        self.event_label.pack(fill="x", pady=2)

        self.screenshot_label = tk.Label(
            self.info_frame,
            text=f"Last Screenshot : {self.stats['last_screenshot']}",
            anchor="w",
            font=("Arial", 11)
        )

        self.screenshot_label.pack(fill="x", pady=2)

        # -----------------------------
        # Refresh Button
        # -----------------------------

        refresh_button = tk.Button(
            self.button_frame,
            text="Refresh Dashboard",
            command=self.refresh_dashboard,
            width=20,
            font=("Arial", 11, "bold")
        )

        refresh_button.pack(pady=10)

    def create_stat_card(
        self,
        parent,
        title,
        value,
        row,
        column
    ):
        """
        Create a reusable dashboard statistic card.

        Parameters
        ----------
        parent : tkinter.Frame
            Parent frame.

        title : str
            Card title.

        value : str | int
            Value to display.

        row : int
            Grid row.

        column : int
            Grid column.
        """

        card = tk.Frame(
            parent,
            relief="solid",
            borderwidth=1,
            padx=15,
            pady=10
        )

        card.grid(
            row=row,
            column=column,
            padx=10,
            pady=10,
            sticky="nsew"
        )

        title_label = tk.Label(
            card,
            text=title,
            font=("Arial", 10, "bold")
        )

        title_label.pack()

        value_label = tk.Label(
            card,
            text=str(value),
            font=("Arial", 18, "bold")
        )

        value_label.pack(pady=(8, 0))

        self.card_labels[title] = value_label

    def run(self):
        """
        Start dashboard.
        """

        self.refresh_dashboard()

        self.root.mainloop()


if __name__ == "__main__":
    dashboard = Dashboard()
    dashboard.run()