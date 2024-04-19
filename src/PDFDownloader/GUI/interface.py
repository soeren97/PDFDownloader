"""User interface."""

import threading
import tkinter as tk
from os.path import abspath
from tkinter import Tk, ttk
from typing import Optional

from PDFDownloader.download import download_all_pdfs
from PDFDownloader.GUI.settings import SettingsWindow
from PDFDownloader.GUI.WidgetBuilder import WidgetBuilder
from PDFDownloader.utils import ConstantsHandler, initialize_repo


class PDFDownloaderGUI:
    """GUI class."""

    def __init__(self, master: Tk) -> None:
        """Initialize class.

        Args:
            master (Tk): Screen.
        """
        self.pdf_folder: Optional[str] = None
        self.data_file: Optional[str] = None
        self.downloaded_file: Optional[str] = None
        self.url_index1: Optional[int] = None
        self.url_index2: Optional[int] = None
        self.timeout: Optional[int] = None
        self.constant_handler: Optional[ConstantsHandler] = None

        self.set_constants()

        self.df = initialize_repo(
            self.downloaded_file,
            self.pdf_folder,
            self.timeout,
        )
        self.master = master
        master.title("Hent pdf'er")

        self.widget_builder = WidgetBuilder(self.master)

        self.create_widgets()

    def create_widgets(self) -> None:
        """Create widgets on the main page."""
        self.speed_label = self.widget_builder.create_label("Tid mellem downloads:")
        self.speed_entry = self.widget_builder.create_entry("5")
        self.submit_button = self.widget_builder.create_button(
            "Hent pdf'er", self.submit
        )
        self.setup_button = self.widget_builder.create_button(
            "Indstillinger", self.setup
        )
        self.cancel_button = self.widget_builder.create_button("Afslut", self.cancel)
        self.progress_bar = self.widget_builder.create_progress_bar()
        self.progress_text = tk.StringVar()
        self.progress_label = self.widget_builder.create_progress_label(
            text_variable=self.progress_text
        )

        # Place widgets on the window
        self.widget_builder.place_widget(
            self.speed_label, row=0, column=0, padx=10, pady=5
        )
        self.widget_builder.place_widget(
            self.speed_entry, row=0, column=1, padx=10, pady=5
        )
        self.widget_builder.place_widget(
            self.submit_button,
            row=1,
            column=0,
            columnspan=2,
            padx=10,
            pady=5,
            sticky="we",
        )
        self.widget_builder.place_widget(
            self.setup_button,
            row=2,
            column=0,
            columnspan=2,
            padx=10,
            pady=5,
            sticky="we",
        )
        self.widget_builder.place_widget(
            self.cancel_button,
            row=3,
            column=0,
            columnspan=2,
            padx=10,
            pady=5,
            sticky="we",
        )
        self.widget_builder.place_widget(
            self.progress_bar,
            row=4,
            column=0,
            columnspan=2,
            padx=10,
            pady=5,
            sticky="we",
        )
        self.widget_builder.place_widget(
            self.progress_label,
            row=5,
            column=0,
            columnspan=2,
            padx=10,
            pady=5,
            sticky="we",
        )

    def set_constants(self) -> None:
        """Set constants in class."""
        self.constant_handler = ConstantsHandler()
        constants = self.constant_handler.constants
        self.pdf_folder = abspath(constants["PDF_folder"])
        self.data_file = abspath(constants["Data_file"])
        self.downloaded_file = abspath(constants["Downloaded_file"])
        self.url_index1 = int(constants["URL_index1"])
        self.url_index2 = int(constants["URL_index2"])
        self.timeout = int(constants["Timeout"])

    def update_progress(self, progress: float) -> None:
        """Update progress bar.

        Args:
            progress (float): Progress percentage.
        """
        self.progress_bar["value"] = progress * 100
        self.progress_text.set(f"{progress * 100:.2f}% Complete")
        self.master.update_idletasks()

    def download_task_threaded(self, delay: int) -> None:
        """Perform download task in a separate thread.

        Args:
            delay (int): Delay between downloads.
        """
        download_all_pdfs(
            self.df,
            delay,
            self.data_file,
            self.url_index1,
            self.url_index2,
            self.pdf_folder,
            self.downloaded_file,
            self.update_progress,
        )

    def submit(self) -> None:
        """Submit button functionality."""
        delay = int(self.speed_entry.get())

        # Update progress bar
        self.progress_bar["value"] = 0
        self.master.update_idletasks()

        threading.Thread(target=self.download_task_threaded, args=(delay,)).start()

        self.df.to_excel(self.downloaded_file, index=True)

    def cancel(self) -> None:
        """Cancel button functionality."""
        self.master.destroy()

    def setup(self) -> None:
        """Excecute setup button."""
        SettingsWindow(self.master, self.constant_handler, self.set_constants)


if __name__ == "__main__":
    pass
