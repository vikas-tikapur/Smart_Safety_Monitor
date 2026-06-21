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

        # Read statistics
        self.stats = self.analytics.get_statistics()

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

        self.create_widgets()

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

    def run(self):
        """
        Start dashboard.
        """

        self.root.mainloop()


if __name__ == "__main__":
    dashboard = Dashboard()
    dashboard.run()