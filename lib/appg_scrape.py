import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import requests
import re
from twitter_scrape import getTwitterURL

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")

driver = webdriver.Chrome(options=chrome_options,
                          executable_path='./chromedriver')

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

    for link in links:
      data = getData(link)
      macro_data.append(data)
    
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


def getChairName(soup):
    name = ""
    
    table = soup.find_all(class_="basicTable")[1]
    rows = table.find_all('p')
    name = rows[5].text 

    return name


def getChairParty(soup):
    party = ""
    
    table = soup.find_all(class_="basicTable")[1]
    rows = table.find_all('p')
    party = rows[6].text 

    return party


def checkBenefits(soup):
    benefits = ""
    
    table = soup.find_all(class_="basicTable")

    if len(table) >= 6:
      source = table[5].find_all('p')[7].text
      benefits = source
    
    return benefits

def getAGM(soup):
    agm = ""

    tables = soup.find_all(class_="basicTable")
    
    if tables[3]:
      words = tables[3].find_all('p')
      agm = words[2].text

    return agm

def getContact(soup):
    contact = ""

    tables = soup.find_all(class_="basicTable")

    if tables[2]:
      words = tables[2].find_all('p')
      
      if 'Email: ' in words[3].text:
        contact = words[3].text.replace("Email: ", "").replace("\n", "")
      else:
        contact = "No email"

    return contact


def getData(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    # Group Name
    group_name = "APPG for " + soup.find(class_="subHead").text

    # Chair name
    chair_name = getChairName(soup)

    # Chair party
    chair_party = getChairParty(soup)

    # Benefits in kind
    benefits_in_kind = checkBenefits(soup)

    # Most recent AGM
    last_agm = getAGM(soup)

    contact = getContact(soup)

    # Twitter
    # twitter_url = getTwitterURL(group_name, driver)

    data = [group_name, chair_name, chair_party, benefits_in_kind, last_agm, contact]
    
    # driver.quit()

    print(data)
    print("\n")
    return data

url = "https://publications.parliament.uk/pa/cm/cmallparty/210310/contents.htm"
callScrape(url)
