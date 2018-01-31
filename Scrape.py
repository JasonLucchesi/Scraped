import logging
import requests
from bs4 import BeautifulSoup

#logging.basicConfig(filename='404.log', level=logging.INFO, format='%(message)s')

# URL to check
url = "http://www.redefinebdl.com/rbh-updates/customer-service-recognition-at-rbh-portfolio-hotels"

result = requests.get(url)

c = result.content
soup = BeautifulSoup(c, 'html.parser')

def pageAlive():
    # Check page is alive
    if (result.status_code == 200):
        print("It's Alive!!!")
    else:
        print("He's dead, Jim!")
        logging.warning('{} - {}'.format(result.status_code, URL))

def pageScrape():
    #Pull HTML
    #print(soup.prettify())

    #Page URL
    print(url)

    #Title Tag
    titleTag = soup.head.title
    print(titleTag)

    #Page Content
    pageContent = soup.find('div', class_='item-page')
    print(pageContent)

    #Images on page
    #Image Path


pageAlive()
pageScrape()

