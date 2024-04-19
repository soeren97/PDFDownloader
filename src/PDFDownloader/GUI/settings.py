"""User interface settings."""

import tkinter as tk
from tkinter import Tk, filedialog
from typing import Callable

from PDFDownloader.GUI.WidgetBuilder import WidgetBuilder
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

        self.widget_builder = WidgetBuilder(self.setup_window)

        self.create_widgets()

    def create_widgets(self) -> None:
        """Create widgets."""
        self.excel_label = self.widget_builder.create_label("Oversigts excel fil:")
        self.excel_entry = self.widget_builder.create_entry(
            self.constant_handler.constants["Data_file"]
        )
        self.excel_button = self.widget_builder.create_button("Find", self.browse_excel)

        self.nsa_label = self.widget_builder.create_label("PDF gemme lokation:")
        self.nsa_entry = self.widget_builder.create_entry(
            self.constant_handler.constants["PDF_folder"]
        )
        self.nsa_button = self.widget_builder.create_button("Find", self.browse_nsa)

        self.downloaded_label = self.widget_builder.create_label(
            "Downloadet checklist:"
        )
        self.downloaded_entry = self.widget_builder.create_entry(
            self.constant_handler.constants["Downloaded_file"]
        )
        self.downloaded_button = self.widget_builder.create_button(
            "Find", self.browse_downloaded
        )

        self.index1_label = self.widget_builder.create_label("PDF URL kolonne nummer:")
        self.index1_entry = self.widget_builder.create_entry(
            str(self.constant_handler.constants["URL_index1"])
        )

        self.index2_label = self.widget_builder.create_label(
            "Report html kolonne nummer:"
        )
        self.index2_entry = self.widget_builder.create_entry(
            str(self.constant_handler.constants["URL_index2"])
        )

        self.timeout_label = self.widget_builder.create_label("Timeout (s):")
        self.timeout_entry = self.widget_builder.create_entry(
            str(self.constant_handler.constants["Timeout"])
        )

        self.save_button = self.widget_builder.create_button(
            "Gem ændringer", self.save_changes
        )
        self.back_button = self.widget_builder.create_button("Tilbage", self.close)

        # Place widgets on the window
        self.place_widgets()

    def place_widgets(self) -> None:
        """Place widgets on the window."""
        self.widget_builder.place_widget(
            self.excel_label, row=0, column=0, padx=10, pady=5
        )
        self.widget_builder.place_widget(
            self.excel_entry, row=0, column=1, padx=10, pady=5
        )
        self.widget_builder.place_widget(
            self.excel_button, row=0, column=2, padx=5, pady=5
        )

        self.widget_builder.place_widget(
            self.nsa_label, row=1, column=0, padx=10, pady=5
        )
        self.widget_builder.place_widget(
            self.nsa_entry, row=1, column=1, padx=10, pady=5
        )
        self.widget_builder.place_widget(
            self.nsa_button, row=1, column=2, padx=5, pady=5
        )

        self.widget_builder.place_widget(
            self.downloaded_label, row=2, column=0, padx=10, pady=5
        )
        self.widget_builder.place_widget(
            self.downloaded_entry, row=2, column=1, padx=10, pady=5
        )
        self.widget_builder.place_widget(
            self.downloaded_button, row=2, column=2, padx=5, pady=5
        )

        self.widget_builder.place_widget(
            self.index1_label, row=3, column=0, padx=10, pady=5
        )
        self.widget_builder.place_widget(
            self.index1_entry, row=3, column=1, padx=10, pady=5
        )

        self.widget_builder.place_widget(
            self.index2_label, row=4, column=0, padx=10, pady=5
        )
        self.widget_builder.place_widget(
            self.index2_entry, row=4, column=1, padx=10, pady=5
        )

        self.widget_builder.place_widget(
            self.timeout_label, row=5, column=0, padx=10, pady=5
        )
        self.widget_builder.place_widget(
            self.timeout_entry, row=5, column=1, padx=10, pady=5
        )

        self.widget_builder.place_widget(
            self.save_button,
            row=6,
            column=0,
            columnspan=3,
            padx=10,
            pady=5,
            sticky="we",
        )
        self.widget_builder.place_widget(
            self.back_button,
            row=7,
            column=0,
            columnspan=3,
            padx=10,
            pady=5,
            sticky="we",
        )

    def browse_excel(self) -> None:
        """Select location of excel file."""
        filename = filedialog.askopenfilename(
            filetypes=(("Excel files", "*.xlsx"), ("All files", "*.*"))
        )
        if filename:
            self.excel_entry.delete(0, tk.END)
            self.excel_entry.insert(tk.END, filename)

    def browse_downloaded(self) -> None:
        """Select location of downloaded file."""
        filename = filedialog.askopenfilename(
            filetypes=(("Excel files", "*.xlsx"), ("All files", "*.*"))
        )
        if filename:
            self.downloaded_entry.delete(0, tk.END)
            self.downloaded_entry.insert(tk.END, filename)

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
        downloaded_location = self.downloaded_entry.get()
        index1 = self.index1_entry.get()
        index2 = self.index2_entry.get()
        timeout = self.timeout_entry.get()

        constants = self.constant_handler.constants

        constants["Data_file"] = excel_location
        constants["PDF_folder"] = nsa_location
        constants["Downloaded_file"] = downloaded_location
        constants["URL_index1"] = index1
        constants["URL_index2"] = index2
        constants["Timeout"] = timeout

        self.constant_handler.update_constants(constants)

    def close(self) -> None:
        """Close window."""
        self.on_close()  # type: ignore
        self.setup_window.destroy()
