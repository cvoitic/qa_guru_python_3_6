import requests
import os


url = 'https://www.selenium.dev/images/sponsors/browserstack.png'
response = requests.get(url=url)
content = response.content

with open('resources/selenium_image.png', 'wb') as file:
    file.write(content)


size = os.path.getsize('resources/selenium_image.png')
assert size == 23783
