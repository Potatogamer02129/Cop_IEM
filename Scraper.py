from bs4 import BeautifulSoup
import requests
def isAvailable(url):
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'html.parser')
    BuyNow = soup.find('button',class_='button button--xl')
    #availability = soup.find('button', class_='button button--xl button--subdued')
    Soldout = soup.find('button', disabled='')
    if Soldout is not None and BuyNow is not None:
        if Soldout.text == 'Sold out' and BuyNow.text != 'Add to cart':
            return False
        else:
            return True
    return None
    #print(availability)
    #print(soup.prettify())

url = 'https://www.headphonezone.in/products/headphone-zone-x-fiio-jd1'
if isAvailable(url):
    print('Available')
else:
    print('Not Available')