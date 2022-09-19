from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def googleSearch(term):
    term = f"define {term}"
    options = webdriver.ChromeOptions()
    options.add_experimental_option(
        'prefs', {'intl.accept_languages': 'en,en_US'})
    driver = webdriver.Chrome(options=options)
    driver.get(f'https://www.google.com/search?q={term}')
    time.sleep(0.05)
    element = driver.find_element(
        By.LINK_TEXT, 'Change to English')
    element.click()

    time.sleep(0.1)
    element2 = driver.find_elements(
        By.CLASS_NAME, 'VwiC3b')
    # element2 = driver.find_elements(By.TAG_NAME, 'span')
    element2 = [item.text for item in element2]
    print(f'there are {len(element2)} results!')
    counter = 1
    for item in (element2):
        print(f'{counter}. {item}')
        counter += 1


googleSearch("Break a leg")
# Z26q7c UK95Uc VGXe8
# By.TAG_NAME
