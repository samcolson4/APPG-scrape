import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import requests
import re

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

def getTwitterURL(name, driver):
    twitterURL = ""
    nameSub = name.replace(" ", "%20")
    src = "&src=typed_query&f=user"
    twitterExplore = "https://twitter.com/search?q="
    
    url = twitterExplore + nameSub + src

    driver.get(url)
    
    timeout = 10
    
    try:
        # THIS IS WORKING: JUST NEED CORRECT CLASS
        element_present = EC.presence_of_element_located((By.CLASS_NAME, 'css-1dbjc4n r-1awozwy r-18u37iz r-1wtj0ep'))
        WebDriverWait(driver, timeout).until(element_present)
        
        if driver.find_elements_by_xpath("//*[contains(text(), 'People')]"):
            print("Found people tab")
    except TimeoutException:
        print("Timed out waiting for page to load")

    # if WebDriverWait(driver, 10).until(driver.find_element_by_class_name("css-1dbjc4n")):
    #     driver.find_element_by_class_name("css-1dbjc4n r-1awozwy r-18u37iz r-1wtj0ep")

    print(driver.current_url)


    return twitterURL
