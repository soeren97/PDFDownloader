"""Function to read excel file."""

from itertools import islice
from typing import Any, Generator

from openpyxl import load_workbook


def read_excel_rows(
    file_path: str, sheet_name: str
) -> Generator[tuple[Any], None, None]:
    """Read rows of an excel file iteratively.

    Args:
        file_path (str): Location of the excel file.
        sheet_name (str): Name of the sheet.

    Yields:
        Generator[tuple[Any]]: Yielded row.
    """
    # Load the Excel workbook
    wb = load_workbook(filename=file_path, read_only=True)
    # Select the worksheet by name
    ws = wb[sheet_name]

    # Iterate over each row in the worksheet, skipping the first row
    for row in islice(ws.iter_rows(values_only=True), 1, None):
        yield row
