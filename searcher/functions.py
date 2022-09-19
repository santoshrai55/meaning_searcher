import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import urllib.request


def internetWorking(host='http://google.com'):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False


# hindi meaning searcher
# result = internetWorking()

# print(result)


def hindiMeaning(term):
    URL = f"https://dict.hinkhoj.com/shabdkhoj.php?word={term}&ie=UTF-8"
    page = requests.get(URL)
    print(f'for hindi meaning: {page}')
    soup = BeautifulSoup(page.content, "html.parser")
    try:
        # searches all the meaning in hindi
        meanings = soup.find_all("a", class_="hin_dict_span")
        # puts them into a list
        meanings = [item.text for item in meanings]
        if len(meanings) > 20:
            meanings = meanings[:20]
        # terms = soup.find_all("div", class_="col-sm-12 dc p-0")[0].text
    except:
        # if no hindi meaning is detected
        meanings = "hindi meaning not found"
    return meanings


# English Meaning Searcher


def englishMeaning(term):
    URL = f'https://www.dictionary.com/browse/{term}'
    page = requests.get(URL)
    print(f'for english meaning: {page}')
    soup = BeautifulSoup(page.content, "html.parser")
    terms = ''
    try:
        terms = soup.find_all(
            "div", class_="e1q3nk1v2")

        # meaning2 = soup.find_all(
        #     "div", class_="css-1o7vb91 e1q3nk1v2")[0].text
        meanings = [meaning.text for meaning in terms]
        if len(meanings) > 5:
            meanings = meanings[:5]

    except:
        meanings = "meaning not found"

    return meanings


def idiomDefination(term):

    URL = f'https://dictionary.cambridge.org/dictionary/{term}'
    page = requests.get(URL)

    print(page)
    soup = BeautifulSoup(page.content, "html.parser")
    terms = ''
    try:
        terms = soup.find_all(
            "div", class_="sense-body dsense_b")

        # meaning2 = soup.find_all(
        #     "div", class_="css-1o7vb91 e1q3nk1v2")[0].text
        meanings = [meaning.text for meaning in terms]
        if len(meanings) > 5:
            meanings = meanings[:5]

    except:
        meanings = "idiom not found"

    return meanings


def googleSearch(term):
    newterm = f"define {term}"
    options = webdriver.ChromeOptions()
    options.add_experimental_option(
        'prefs', {'intl.accept_languages': 'en,en_US'})
    driver = webdriver.Chrome(options=options)
    driver.get(f'https://www.google.com/search?q={newterm}')

    # Changes language to English
    element = driver.find_element(
        By.LINK_TEXT, 'Change to English')
    element.click()
    print('changed to English')
    time.sleep(0.05)
    print('selecting the definations')
    # Searches definations
    element2 = driver.find_elements(
        By.CLASS_NAME, 'VwiC3b')

    # Converts the results in to a list
    definations = [item.text for item in element2]
    definations = definations[1:4]
    # for each in definations:
    #     print(each)

    print('searching the images')
    # Searches images
    driver.get(f'https://www.google.com/search?q={term}&tbm=isch&ved')
    time.sleep(0.05)
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
