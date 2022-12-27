import os.path
import time

from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 1
# options = webdriver.ChromeOptions()
# prefs = {
#     'download.default_directory': '/Users/Cristina Voitic/PycharmProjects/qa_guru_python_3_6/tmp',
#     'download.prompt_for_download': False
# }
# options.add_experimental_option('prefs', prefs)
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# browser.config.driver = driver
#
# browser.open('https://demoqa.com/upload-download')
# browser.element('#downloadButton').click()
# time.sleep(1)

# assert os.path.getsize('tmp/sampleFile.jpeg') == 4096
# os.remove('tmp/sampleFile.jpeg')

# 2 with abs_path
current_dir = os.path.dirname(os.path.abspath(__file__))
tmp_dir = os.path.join(current_dir, '../tmp')
options = webdriver.ChromeOptions()
prefs = {
    'download.default_directory': tmp_dir,
    'download.prompt_for_download': False
}
options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
browser.config.driver = driver

browser.open('https://demoqa.com/upload-download')
browser.element('#downloadButton').click()
time.sleep(2)
samplefile = os.path.join(tmp_dir, 'sampleFile.jpeg')
assert os.path.getsize(samplefile) == 4096
# os.remove(samplefile)

# упростили код ввели переменную samplefile assert os.path.getsize(os.path.join(tmp_dir, 'sampleFile.jpeg')) == 4096
# os.remove(os.path.join(tmp_dir, 'sampleFile.jpeg'))