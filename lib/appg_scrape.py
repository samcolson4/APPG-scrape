import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import requests
import re

def callScrape(url):
    macro_data = []
    
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    block = soup.find(id="mainTextBlock")
    
    groups = block.find_all('ul')
    countries = groups[0]
    subjects = groups[1]

    country_links = getLinks(countries)
    subject_links = getLinks(subjects)

    links = country_links + subject_links
    
    return macro_data


def getLinks(block):
    links = []

    for group in block:

        link = group.find('a')

        if type(link) is int:
          group_link = "void"
        else:
          href = link.get('href')
          group_link = "https://publications.parliament.uk/pa/cm/cmallparty/210310/" + href
          links.append(group_link)

    return links


url = "https://publications.parliament.uk/pa/cm/cmallparty/210310/contents.htm"
callScrape(url)


# how many tweets in past week