# PDFDownloader
PDFDownloader is a simple graphical user interface (GUI) application designed to download PDF files from URLs listed in an Excel file. This tool offers flexibility in download management through a customizable download delay and a settings window for adjusting folder and file locations, as well as other file-specific settings.

## Usage

1. Ensure that an Excel file containing the URLs of the PDF files you wish to download is placed in the "Data/" folder within the repository.

2. Run the application.

3. Set the desired download delay in seconds. A delay of 0 allows for maximum download speed, while higher delay values limit the download rate to one file per specified interval.

4. Optionally, utilize the settings window to configure folder and file locations, as well as other settings relevant to your download preferences.

5. Start the download process. PDF files will be downloaded sequentially from the URLs listed in the Excel file.

## Installation Guide

### Prerequisites:
- Anaconda or miniconda installed.
- `GRI_2017_2020.xlsx` in a folder called `Data/`. The data can be found here: `https://docs.google.com/spreadsheets/d/1mkkHaJk88GALh7ElTUp7x-PXIO9RP41G/edit?usp=sharing&ouid=114880054188119378404&rtpof=true&sd=true`

### Steps:

1. **Clone the Repository:**
`git clone https://github.com/soeren97/PDFDownloader`

2. **Navigate to the Repository Directory:**
`cd */PDFDownloader`

3. **Create a Virtual Environment (Optional but Recommended):**
`conda create -n your-env-name python=3.11`

4. **Activate the Virtual Environment:**
`conda activate your-env-name`

5. **Install Required Packages:**
`pip install .`

6. **Verify Installation:**
Ensure all dependencies are installed successfully without any errors.

7. **Deactivate Virtual Environment (If Created):**
`conda deactivate`

8. **Create config.json.**
Create a file containing the fields username and password in the repocetory directory.


### Additional Notes:

- **Virtual Environment:** Creating a virtual environment is a good practice to isolate project dependencies from other projects and the system Python environment.
- **pip Install:** The `pip install .` command installs the necessary packages specified in the `setup.py` file from the current directory.
- **requirements** The required packages can be found in the `setup.py` file as the variable `INSTALL_REQQUIRES`.
