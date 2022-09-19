from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def googleSearch(term):
    newterm = f"define {term}"
    options = webdriver.ChromeOptions()
    options.add_experimental_option(
        'prefs', {'intl.accept_languages': 'en,en_US'})
    driver = webdriver.Chrome(options=options)
    driver.get(f'https://www.google.com/search?q={newterm}')
    time.sleep(0.05)

    # Changes language to English
    element = driver.find_element(
        By.LINK_TEXT, 'Change to English')
    element.click()

    time.sleep(0.1)

    # Searches definations
    element2 = driver.find_elements(
        By.CLASS_NAME, 'VwiC3b')

    # Converts the results in to a list
    definations = [item.text for item in element2]
    definations = definations[1:]

    # Searches images
    driver.get(f'https://www.google.com/search?q={term}&tbm=isch&ved')
    time.sleep(0.1)
    images = driver.find_elements(
        By.TAG_NAME, "img")
    # converts image links to a list
    images_list = [str(item.get_attribute('src')) for item in images]

    # filters out the unneccessary results
    image_links = []
    for item in images_list:
        if "encrypted" in item:
            image_links.append(item)

    results = [definations, image_links]
    return results
