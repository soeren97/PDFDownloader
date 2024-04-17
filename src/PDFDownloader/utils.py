"""Utility functions."""

import os
import socket

import pandas as pd

from PDFDownloader.constants import DOWNLOADED_FILE, PDF_FOLDER, TIMEOUT


def initialize_repo() -> pd.DataFrame:
    """Initialize the repocetory.

    Returns:
        pd.DataFrame: Overview of downloaded pdfs.
    """
    os.makedirs(PDF_FOLDER, exist_ok=True)

    socket.setdefaulttimeout(TIMEOUT)

    if not os.path.isfile(DOWNLOADED_FILE):
        return pd.DataFrame(columns=["Downloaded", "Error 1", "Error 2"])
    else:
        df = pd.read_excel(DOWNLOADED_FILE, index_col=0)
        return df


if __name__ == "__main__":
    pass
