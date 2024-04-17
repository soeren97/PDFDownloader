"""Functions to download pdfs."""

import os.path as path
import socket
import time
import urllib.error
import urllib.request
from typing import Optional, Union
from urllib.error import URLError

import pandas as pd

from PDFDownloader.read_excel import read_excel_rows


def download_all_pdfs(
    df: pd.DataFrame,
    delay: int,
    data_file: str,
    url_index1: int,
    url_index2: int,
    pdf_folder: str,
) -> pd.DataFrame:
    """Download all pdfs.

    Args:
        df (pd.DataFrame): Overview of downloaded pdfs.

    Returns:
        pd.DataFrame: Overview of downloaded pdfs.
    """
    for row in read_excel_rows(data_file, "0"):
        start_time = time.time()
        br_number = row[0]
        if br_number in df.index:
            if df.loc[br_number]["Downloaded"]:
                continue

        pdf_url1 = row[url_index1]
        pdf_url2 = row[url_index2]

        save_path = path.join(pdf_folder, f"{br_number}.pdf")

        try:
            error1 = download_pdf(pdf_url1, pdf_url2, save_path)
        except (urllib.error.URLError, socket.timeout) as error2:
            # File is not downloaded
            df.loc[br_number] = [False, error1, error2]

        # File is downloaded.
        df.loc[br_number] = [True, None, None]
        time_spent = time.time() - start_time
        if time_spent < delay:
            time.sleep(delay - time_spent)
        break
    return df


def download_pdf(
    pdf_url1: str, pdf_url2: str, save_path: str
) -> Optional[Union[URLError, TimeoutError]]:
    """Download a pdf using one of two urls.

    Args:
        pdf_url1 (str): First url.
        pdf_url2 (str): Second url.
        save_path (str): Save location of pdf.

    Returns:
        Optional[URLError]: Error from retriving url.
    """
    try:
        urllib.request.urlretrieve(pdf_url1, save_path)
    except (urllib.error.URLError, socket.timeout) as e:
        urllib.request.urlretrieve(pdf_url2, save_path)
        return e
    return None


if __name__ == "__main__":
    pass
