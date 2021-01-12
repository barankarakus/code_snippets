import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# path to chromedriver executable
CHROMEDRIVER_PATH = '/usr/local/bin/chromedriver'
# directory to download PDFs to
DOWNLOAD_DIR = '/Users/barankarakus/Documents'
# options ensure that if a pdf is loaded, it is automatically downloaded to
# DOWNLOAD_DIR, rather than opened and viewed in the browser
chrome_options = Options()
chrome_options.add_experimental_option('prefs',  {
    "download.default_directory": DOWNLOAD_DIR
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True
    }
)
# create driver
driver = webdriver.Chrome(
    executable_path=CHROMEDRIVER_PATH,
    options=chrome_options
)
# go to link to PDF
driver.get(
    ''  # replace with link to PDF
)
# if doing lots of PDF downloads, give a moment for the download to complete (can probably do this waiting more intelligently)
time.sleep(2)

# PDF will be downloaded to DOWNLOAD_DIR (with the same name it has on the website, e.g. https://www.../just_some_pdf.pdf will be downloaded as just_some_pdf.pdf)
