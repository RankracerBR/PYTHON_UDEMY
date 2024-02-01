from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

#Chrome options (search site)

ROOT_FOLDER = Path(__file__).parent
CHROME_DRIVER_PATH = ROOT_FOLDER / 'drivers' / 'chromedriver.exe'

def make_chrome_browser(*options: str) -> webdriver.Chrome: 
    chrome_options = webdriver.ChromeOptions()

    if options is not None:
        for option in options:
            chrome_options.add_argument(option) # type: ignore

    chrome_service = Service(
        executable_path=str(CHROME_DRIVER_PATH)
    )

    browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options
    )

    return browser


if __name__ == '__main__':

    options = '--headless', '--disable-gpu',
    browser = make_chrome_browser(*options)

    browser.get('https://www.google.com')

    time.sleep(10)