"""Functions to download pdfs."""

import os.path as path
import urllib.error
import urllib.request

import pandas as pd

from PDFDownloader.constants import DATA_FILE, PDF_FOLDER, URL_INDEX_1, URL_INDEX_2
from PDFDownloader.read_excel import read_excel_rows


def download_all_pdfs(df: pd.DataFrame) -> pd.DataFrame:
    """Download all pdfs.

    Args:
        df (pd.DataFrame): Overview of downloaded pdfs.

    Returns:
        pd.DataFrame: Overview of downloaded pdfs.
    """
    for row in read_excel_rows(DATA_FILE, "0"):
        br_number = row[0]
        if br_number in df.index:
            if df.loc[br_number]:
                continue

        pdf_url = row[URL_INDEX_1]
        save_path = path.join(PDF_FOLDER, f"{br_number}.pdf")

        try:
            urllib.request.urlretrieve(pdf_url, save_path)
        except urllib.error.URLError:
            try:
                pdf_url = row[URL_INDEX_2]
                urllib.request.urlretrieve(pdf_url, save_path)
            except urllib.error.URLError:
                continue

        # File is downloaded.
        df.loc[br_number] = True
        break
    return df


if __name__ == "__main__":
    pass
