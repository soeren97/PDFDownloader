"""User interface settings."""

import tkinter as tk
from tkinter import Tk, filedialog


class SettingsWindow:
    """Settings window class."""

    def __init__(self, master: Tk):
        """Initialize class.

        Args:
            master (Tk): Window.
        """
        self.master = master
        self.setup_window = tk.Toplevel(master)
        self.setup_window.title("Indstillinger")
        self.setup_window.grab_set()

        self.excel_label = tk.Label(self.setup_window, text="Excel Lokation:")
        self.excel_label.grid(row=0, column=0, padx=10, pady=5)

        self.excel_entry = tk.Entry(self.setup_window)
        self.excel_entry.grid(row=0, column=1, padx=10, pady=5)

        self.excel_button = tk.Button(
            self.setup_window, text="Find", command=self.browse_excel
        )
        self.excel_button.grid(row=0, column=2, padx=5, pady=5)

        self.nsa_label = tk.Label(self.setup_window, text="PDF Gemme lokation:")
        self.nsa_label.grid(row=1, column=0, padx=10, pady=5)

        self.nsa_entry = tk.Entry(self.setup_window)
        self.nsa_entry.grid(row=1, column=1, padx=10, pady=5)

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
            self.setup_window, text="Tilbage", command=self.setup_window.destroy
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
        nsa_location = self.nsa_entry.get()  # TODO: save changes.
        # Do something with the locations, like save them
        print("Excel Location:", excel_location)
        print("NSA Location:", nsa_location)
