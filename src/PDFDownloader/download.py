"""Functions to download pdfs."""

import os.path as path
import socket
import time
import urllib.error
import urllib.request
from typing import Callable, Optional, Union
from urllib.error import URLError

import pandas as pd

from PDFDownloader.read_excel import count_excel_rows, read_excel_rows


def download_all_pdfs(
    df: pd.DataFrame,
    delay: int,
    data_file: str,
    url_index1: int,
    url_index2: int,
    pdf_folder: str,
    downloaded_file: str,
    progress_callback: Optional[Callable[[float], None]] = None,
) -> pd.DataFrame:
    """Download all pdfs.

    Args:
        df (pd.DataFrame): Overview of downloaded pdfs.
        delay (int): Download delay.
        data_file (str): Overview of desired pdfs.
        url_index1 (int): Index of download url1.
        url_index2 (int): Index of download url2.
        pdf_folder (str): Folder where pdfs should be saved.
        downloaded_file (str): File to keep track of downloaded files.
        progress_callback (Optional[Callable[[float], None]], optional):
            Callback to update progressbar. Defaults to None.

    Returns:
        pd.DataFrame: Overview of downloaded pdf.
    """
    total_rows = count_excel_rows(data_file, "0")
    rows_downloaded = 0

    for row in read_excel_rows(data_file, "0"):
        start_time = time.time()
        br_number = row[0]
        if br_number in df.index:
            if df.loc[br_number]["Downloaded"]:
                if progress_callback:
                    rows_downloaded = update_progress(
                        total_rows, rows_downloaded, progress_callback
                    )
                continue

        pdf_url1 = row[url_index1]
        pdf_url2 = row[url_index2]

        save_path = path.join(pdf_folder, f"{br_number}.pdf")

        result = download_pdf(pdf_url1, pdf_url2, save_path)

        df.loc[br_number] = result

        if progress_callback:
            rows_downloaded = update_progress(
                total_rows, rows_downloaded, progress_callback
            )

        # Save the updated DataFrame to Excel
        df.to_excel(downloaded_file, index=True)

        time_spent = time.time() - start_time
        if time_spent < delay:
            time.sleep(delay - time_spent)
    return df


def download_pdf(
    pdf_url1: str, pdf_url2: str, save_path: str
) -> list[
    Union[
        bool,
        Optional[Union[URLError, TimeoutError, TypeError]],
        Optional[Union[URLError, TimeoutError, TypeError]],
    ]
]:
    """Download a pdf using one of two urls.

    Args:
        pdf_url1 (str): First url.
        pdf_url2 (str): Second url.
        save_path (str): Save location of pdf.

    Returns:
        list[
        bool,
        Optional[Union[URLError, TimeoutError, TypeError]],
        Optional[Union[URLError, TimeoutError, TypeError]],
        ]: Result of queries.
    """
    error1 = None
    error2 = None
    try:
        urllib.request.urlretrieve(pdf_url1, save_path)
    except (urllib.error.URLError, socket.timeout, TypeError) as e1:
        error1 = e1
        try:
            urllib.request.urlretrieve(pdf_url2, save_path)
        except (urllib.error.URLError, socket.timeout, TypeError) as e2:
            error2 = e2
            return [False, error1, error2]
    return [True, error1, error2]


def update_progress(
    total_rows: int,
    rows_downloaded: int,
    progress_callback: Optional[Callable[[float], None]] = None,
) -> int:
    """Update progress.

    Args:
        total_rows (int): Total number of rows in excel file.
        rows_downloaded (int): Number of rows already downloaded.
        progress_callback (Optional[Callable[[float], None]], optional):
            Function to update progressbar. Defaults to None.

    Returns:
        int: Number of rows downloaded.
    """
    rows_downloaded += 1
    progress = rows_downloaded / total_rows
    progress_callback(progress)  # type:ignore
    return rows_downloaded


if __name__ == "__main__":
    pass
