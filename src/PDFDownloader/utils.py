"""Utility functions."""

import json
import os
import socket
from typing import Any, Optional

import pandas as pd


class ConstantsHandler:
    """Handle all constant manipulation."""

    def __init__(self) -> None:
        """Initialize class."""
        self.constants: Optional[dict[str, Any]] = None
        self.read_json()

    def read_json(self) -> None:
        """Read constants."""
        with open("constants.json", "r") as f:
            self.constants = json.load(f)

    def save_json(self) -> None:
        """Save changes to constants."""
        with open("constants.json", "w") as f:
            json.dump(self.constants, f, indent=4)

    def update_constants(self, constants: dict[str, Any]) -> None:
        """Update the constants file.

        Args:
            constants (dict[str]): Constants.
        """
        self.constants = constants
        self.save_json()


def initialize_repo(download_file: str, pdf_folder: str, timeout: int) -> pd.DataFrame:
    """Initialize the repocetory.

    Returns:
        pd.DataFrame: Overview of downloaded pdfs.
    """
    os.makedirs(pdf_folder, exist_ok=True)

    socket.setdefaulttimeout(timeout)

    if not os.path.isfile(download_file):
        return pd.DataFrame(columns=["Downloaded", "Error 1", "Error 2"])
    else:
        df = pd.read_excel(download_file, index_col=0)
        return df


if __name__ == "__main__":
    pass
