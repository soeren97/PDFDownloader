"""Class for creating widgets."""

import tkinter as tk
from tkinter import ttk
from typing import Any, Callable, Optional


class WidgetBuilder:
    """A utility class for building tkinter widgets."""

    def __init__(self, master: tk.Tk):
        """Initialize the WidgetBuilder.

        Args:
            master (tk.Tk): The root window.
        """
        self.master = master

    def create_label(self, text: str) -> tk.Label:
        """Create a Label widget.

        Args:
            text (str): The text to display on the label.

        Returns:
            tk.Label: The created Label widget.
        """
        label = tk.Label(self.master, text=text)
        return label

    def create_entry(self, default_text: str) -> tk.Entry:
        """Create an Entry widget.

        Args:
            default_text (str): The default text to display in the entry.

        Returns:
            tk.Entry: The created Entry widget.
        """
        entry = tk.Entry(self.master)
        entry.insert(0, default_text)
        return entry

    def create_button(self, text: str, command: str | Callable[[], Any]) -> tk.Button:
        """Create a Button widget.

        Args:
            text (str): The text to display on the button.
            command (str | Callable[[], Any]): The function to call when
                the button is clicked.

        Returns:
            tk.Button: The created Button widget.
        """
        button = tk.Button(self.master, text=text, command=command)
        return button

    def create_progress_bar(self) -> ttk.Progressbar:
        """Create a Progressbar widget.

        Returns:
            ttk.Progressbar: The created Progressbar widget.
        """
        progress_bar = ttk.Progressbar(
            self.master, orient="horizontal", mode="determinate"
        )
        return progress_bar

    def create_progress_label(self, text_variable: tk.Variable) -> tk.Label:
        """Create a Label widget to display progress.

        Args:
            text_variable (tk.Variable):
                The StringVar to bind to the label's text. Defaults to None.

        Returns:
            tk.Label: The created Label widget.
        """
        progress_label = tk.Label(self.master, textvariable=text_variable)
        return progress_label

    def place_widget(
        self,
        widget: Any,
        row: int,
        column: int,
        rowspan: int = 1,
        columnspan: int = 1,
        padx: int = 0,
        pady: int = 0,
        sticky: str = "",
    ) -> None:
        """Place a widget on the window.

        Args:
            widget (Any): The widget to place.
            row (int): The row index to place the widget in.
            column (int): The column index to place the widget in.
            rowspan (int, optional): The number of rows that the widget occupies.
                Defaults to 1.
            columnspan (int, optional): The number of columns that the widget occupies.
                Defaults to 1.
            padx (int, optional): Padding in the x-direction. Defaults to 0.
            pady (int, optional): Padding in the y-direction. Defaults to 0.
            sticky (str, optional): How the widget should stick to the cell.
                Defaults to "".
        """
        widget.grid(
            row=row,
            column=column,
            rowspan=rowspan,
            columnspan=columnspan,
            padx=padx,
            pady=pady,
            sticky=sticky,
        )
