import os
from distutils.util import strtobool
from Scraper2 import isAvailable
from BotmsgHTTP import notify
url = 'https://www.headphonezone.in/products/headphone-zone-x-fiio-jd1'

current_status = isAvailable(url)
if os.path.isfile('last.txt'):
    with open('last.txt','r') as f:
        previous_status = strtobool(f.read().strip())
else:
    previous_status = False

if previous_status == False and current_status:
    notify(url)
    print('Notifying')

with open('last.txt','w') as f:
    f.write(str(current_status))