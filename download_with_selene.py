import time

from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
prefs = {
    'download.default_directory': '/Users/Cristina Voitic/PycharmProjects/qa_guru_python_3_6/tmp',
    'download.prompt_for_download': False
}
options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
browser.config.driver = driver

browser.open('https://demoqa.com/upload-download')
browser.element('#downloadButton').click()
time.sleep(1)

assert os.path.getsize('tmp/sampleFile.jpeg') == 4096