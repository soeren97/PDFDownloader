"""The main loop."""

from PDFDownloader.constants import DOWNLOADED_FILE
from PDFDownloader.download import download_all_pdfs
from PDFDownloader.utils import initialize_repo


def main() -> None:
    """Run the main loop."""
    df = initialize_repo()

    download_all_pdfs(df)

    df.to_excel(DOWNLOADED_FILE, index=True)


if __name__ == "__main__":
    main()
