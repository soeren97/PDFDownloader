"""Constants used in the repocetory."""

import os.path as path

DATA_FOLDER = "Data/"
PDF_FOLDER = path.join(DATA_FOLDER, "Reports/")

DATA_FILE = path.join(DATA_FOLDER, "GRI_2017_2020.xlsx")
METADATA_FILE = path.join(DATA_FOLDER, "Metadata2006_2016.xlsx")
DOWNLOADED_FILE = path.join(DATA_FOLDER, "downloaded.xlsx")


URL_INDEX_1 = 37
URL_INDEX_2 = 38

TIMEOUT = 5

if __name__ == "__main__":
    pass
