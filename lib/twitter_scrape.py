import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import requests
import re

def getTwitterURL(url):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0'}
    

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    print(soup)

    urls = soup.find_all(class_="tF2Cxc")
    print(urls)
    twitterURL = ""
    

    return twitterURL