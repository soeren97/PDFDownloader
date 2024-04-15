"""The main loop."""

import tkinter as tk

from PDFDownloader.GUI.interface import PDFDownloaderGUI


def main() -> None:
    """Run the GUI."""
    root = tk.Tk()
    PDFDownloaderGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
