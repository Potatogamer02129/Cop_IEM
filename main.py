import os
from distutils.util import strtobool
from Scraper2 import isAvailable

url = 'https://www.headphonezone.in/products/headphone-zone-x-fiio-jd1'

current_status = isAvailable(url)
print(current_status)
if os.path.exists('last.txt'):
    if current_status:
        with open('last.txt','r') as f:
            previous_status = strtobool(f.read().strip())
            print(previous_status)
            if previous_status and current_status:
                with open('last.txt','w') as f:
                    f.write(str(previous_status))
            elif previous_status == False and current_status:
                #Send Notification
                print('Notifying')
                with open('last.txt','w') as f:
                    f.write(str(current_status))
    else:
        with open('last.txt','w') as f:
            f.write(str(current_status))
with open('last.txt', 'w') as f:
        f.write(str(current_status))
