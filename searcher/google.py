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

    driver.get(f'https://www.google.com/search?q={term}&tbm=isch&ved')
    # img = driver.find_element(
    #     By.LINK_TEXT, 'Images')
    # img.click()
    time.sleep(0.1)
    images = driver.find_elements(
        By.TAG_NAME, "img")
    images_list = [str(item.get_attribute('src')) for item in images]

    # filtered_images = []
    # filter_text = "encrypted"
    # for item in images_list:
    #     if filter_text in item:
    #         filtered_images.append(item)

    # print(filtered_images)
    newimage = []

    for item in images_list:
        if "encrypted" in item:
            newimage.append(item)
    print(f'there are {len(newimage)} in the images.')
    for each in newimage:
        print(each)


googleSearch("Mother")
# Z26q7c UK95Uc VGXe8
# By.TAG_NAME
# By.LINK_TEXT
# new_list = [item for item in my_list if substring not in item]
