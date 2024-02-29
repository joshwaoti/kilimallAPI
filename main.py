from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_argument("headless")
driver = webdriver.Chrome(options=options)

driver.get('https://www.kilimall.co.ke/new/')

page_source = driver.page_source

soup = BeautifulSoup(page_source, "html.parser")

# items = driver.find_elements(class_="price")
elements = soup.find_all(class_="product")

for element in elements:
    # Extracting title
    title_element = element.find(class_='title')
    title = title_element.get_text(strip=True) if title_element else None

    # Extracting ID from the href attribute
    id = element.a['href'].split('/')[-1].split('-')[0] if element.a else None

    # Extracting price
    price_element = element.find(class_='price')
    price = price_element.get_text(strip=True) if price_element else None

    # Extracting info (optional, adjust as needed)
    info_element = element.find(class_='info')
    info = info_element.get_text(strip=True) if info_element else None

    # Extracting link
    link = element.a['href'] if element.a else None

    # Printing or saving the extracted information
    print(f"Title: {title}")
    print(f"ID: {id}")
    print(f"Price: {price}")
    print(f"Info: {info}")
    print(f"Link: {link}")
    print()




ls = ["title","price"]
# text_elements = [element.get_text(strip=True) for element in elements]

name_elements = soup.select('.title')
price_elements = soup.select('.price')


# Scroll down the page
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

time.sleep(3)

driver.quit()