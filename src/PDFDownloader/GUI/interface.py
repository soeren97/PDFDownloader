"""User interface."""

import tkinter as tk
from tkinter import Tk

from PDFDownloader.constants import DOWNLOADED_FILE
from PDFDownloader.download import download_all_pdfs
from PDFDownloader.GUI.settings import SettingsWindow
from PDFDownloader.utils import initialize_repo


class PDFDownloaderGUI:
    """GUI class."""

    def __init__(self, master: Tk) -> None:
        """Initialize class.

        Args:
            master (Tk): Screen.
        """
        self.df = initialize_repo()
        self.master = master
        master.title("Hent pdf'er")

        self.speed_label = tk.Label(master, text="Tid mellem downloads:")
        self.speed_label.grid(row=0, column=0, padx=10, pady=5)

        self.speed_entry = tk.Entry(master)
        self.speed_entry.grid(row=0, column=1, padx=10, pady=5)

        default_speed = "10"

        self.speed_entry = tk.Entry(master)
        self.speed_entry.insert(0, default_speed)  # Inserting default value
        self.speed_entry.grid(row=0, column=1, padx=10, pady=5)

        self.submit_button = tk.Button(master, text="Hent pdf'er", command=self.submit)
        self.submit_button.grid(
            row=1, column=0, columnspan=2, padx=10, pady=5, sticky="we"
        )

        self.setup_button = tk.Button(master, text="Indstillinger", command=self.setup)
        self.setup_button.grid(
            row=2, column=0, columnspan=2, padx=10, pady=5, sticky="we"
        )

        self.cancel_button = tk.Button(master, text="Afslut", command=self.cancel)
        self.cancel_button.grid(
            row=3, column=0, columnspan=2, padx=10, pady=5, sticky="we"
        )

    def submit(self) -> None:
        """Submit button functionality."""
        delay = int(self.speed_entry.get())

        self.df = download_all_pdfs(self.df, delay)

        self.df.to_excel(DOWNLOADED_FILE, index=True)

    def cancel(self) -> None:
        """Cancel button functionality."""
        self.master.destroy()

    def setup(self) -> None:
        """Excecute setup button."""
        SettingsWindow(self.master)


if __name__ == "__main__":
    pass
