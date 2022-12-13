import requests

url = 'https://www.selenium.dev/images/sponsors/browserstack.png'
response = requests.get(url=url)
content = response.content

with open('selenium_image.png', 'wb') as file:
    file.write(content)

import os
size = os.path.getsize('selenium_image.png')
assert size == 23783