from bs4 import BeautifulSoup
import requests
def isAvailable(url):
    source = requests.get(url,timeout=10).text
    soup = BeautifulSoup(source, 'html.parser')
    available = soup.find('button',type='submit')
    if available is None:
        return False
    txt = available.text.strip().lower()
    if 'disabled' in available.attrs:
        return False
    elif 'disabled' not in available.attrs and txt == 'add to cart':
        return True
    return False
if __name__ == '__main__':
    url = 'https://www.headphonezone.in/products/moondrop-chu-ii-unboxed'
    if isAvailable(url):
        print('Available')
    else:
        print('Not Available')