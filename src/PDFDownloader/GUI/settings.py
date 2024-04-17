"""User interface settings."""

import tkinter as tk
from tkinter import Tk, filedialog
from typing import Callable

from PDFDownloader.utils import ConstantsHandler


class SettingsWindow:
    """Settings window class."""

    def __init__(
        self,
        master: Tk,
        constant_handler: ConstantsHandler,
        on_close: Callable[[None], None],
    ):
        """Initialize class.

        Args:
            master (Tk): Window.
        """
        self.master = master
        self.constant_handler = constant_handler
        self.on_close = on_close

        self.setup_window = tk.Toplevel(master)
        self.setup_window.title("Indstillinger")
        self.setup_window.grab_set()

        self.excel_label = tk.Label(self.setup_window, text="Oversigts excel fil:")
        self.excel_label.grid(row=0, column=0, padx=10, pady=5)

        self.excel_entry = tk.Entry(self.setup_window)
        self.excel_entry.grid(row=0, column=1, padx=10, pady=5)
        self.excel_entry.insert(0, self.constant_handler.constants["Data_file"])

        self.excel_button = tk.Button(
            self.setup_window, text="Find", command=self.browse_excel
        )
        self.excel_button.grid(row=0, column=2, padx=5, pady=5)

        self.nsa_label = tk.Label(self.setup_window, text="PDF gemme lokation:")
        self.nsa_label.grid(row=1, column=0, padx=10, pady=5)

        self.nsa_entry = tk.Entry(self.setup_window)
        self.nsa_entry.grid(row=1, column=1, padx=10, pady=5)
        self.nsa_entry.insert(0, self.constant_handler.constants["PDF_folder"])

        self.nsa_button = tk.Button(
            self.setup_window, text="Find", command=self.browse_nsa
        )
        self.nsa_button.grid(row=1, column=2, padx=5, pady=5)

        self.save_button = tk.Button(
            self.setup_window, text="Gem ændringer", command=self.save_changes
        )
        self.save_button.grid(
            row=2, column=0, columnspan=3, padx=10, pady=5, sticky="we"
        )

        self.back_button = tk.Button(
            self.setup_window, text="Tilbage", command=self.close
        )
        self.back_button.grid(
            row=3, column=0, columnspan=3, padx=10, pady=5, sticky="we"
        )

    def browse_excel(self) -> None:
        """Select location of excel file."""
        filename = filedialog.askopenfilename(
            filetypes=(("Excel files", "*.xlsx"), ("All files", "*.*"))
        )
        if filename:
            self.excel_entry.delete(0, tk.END)
            self.excel_entry.insert(tk.END, filename)

    def browse_nsa(self) -> None:
        """Select location of NSA."""
        filename = filedialog.askdirectory()
        if filename:
            self.nsa_entry.delete(0, tk.END)
            self.nsa_entry.insert(tk.END, filename)

    def save_changes(self) -> None:
        """Save changes made."""
        excel_location = self.excel_entry.get()
        nsa_location = self.nsa_entry.get()

        constants = self.constant_handler.constants

        constants["Data_file"] = excel_location
        constants["PDF_folder"] = nsa_location

        self.constant_handler.update_constants(constants)

    def close(self) -> None:
        """Close window."""
        self.on_close()  # type: ignore
        self.setup_window.destroy()
