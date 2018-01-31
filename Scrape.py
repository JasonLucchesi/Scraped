import logging
import requests
from bs4 import BeautifulSoup

logging.basicConfig(filename='404.log', level=logging.INFO, format='%(message)s')

# URL to check
url = "http://www.redefinebdl.com/rbh-updates/customer-service-recognition-at-rbh-portfolio-hotels"
result = requests.get(url)

def pageAlive():
    # Check page is alive
    if (result.status_code == 200):
        print("It's Alive!!!")
    else:
        print("He's dead, Jim!")
        logging.warning('{} - {}'.format(result.status_code, URL))

def pageContent():
    #Pull HTML
    c = result.content
    soup = BeautifulSoup(c, 'html.parser')
    print(soup.prettify())

pageAlive()
pageContent()