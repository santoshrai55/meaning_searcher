from bs4 import BeautifulSoup
import requests
import pyperclip
import keyboard
import time


term = "harmonious"


def hindiMeaning(term):
    URL = f"https://dict.hinkhoj.com/shabdkhoj.php?word={term}&ie=UTF-8"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    try:
        terms = soup.find_all("a", class_="hin_dict_span")
        terms = [item.text for item in terms]
        # terms = soup.find_all("div", class_="col-sm-12 dc p-0")[0].text
    except:
        terms = "meaning not found"

    return terms


result = hindiMeaning(term)
print(result)
