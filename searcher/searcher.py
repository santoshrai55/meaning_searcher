from bs4 import BeautifulSoup
import pyperclip

import requests
import keyboard
import time


def searcher():

    hotkey = "shift + F1"

    while True:

        if keyboard.is_pressed(hotkey):
            # pyauto.typewrite('Hello world!')
            term = pyperclip.paste()
            print(f'this is the term: {term}')
            print("The term has been copied!")
            URL = f'https://www.dictionary.com/browse/{term}'

            print("Looking for the term ...")
            # ctrl-c is usually very fast but your program may execute faster
            time.sleep(.01)

            if term != "":
                page = requests.get(URL)
                print(page)
                time.sleep(0.10)
                soup = BeautifulSoup(page.content, "html.parser")
                terms = ''
                try:
                    terms = soup.find_all(
                        "section", class_="css-109x55k e1hk9ate4")[0].text
                except:
                    terms = "meaning not found"
                terms2 = ''

                try:
                    terms2 = soup.find_all(
                        "section", class_="css-109x55k e1hk9ate4")[1].text
                except:
                    terms = "second meaning not found"

                final_term = terms+terms2
                final_term = final_term.replace('etc.:', 'etc:\n')
                final_term = final_term.replace('.', '\n')
                final_term = final_term.replace('noun', 'NOUN: \n')
                final_term = final_term.replace('verb', '\n\nVERB: \n')
                final_term = final_term.replace('SEE MORESEE LESS', ' ')
                time.sleep(0.05)
                # print("--------RESULT--------")
                # print(final_term)
                # print("--------------------")
                result = {'term': term, 'final_term': final_term}
                return result

            else:
                print("The string is empty!")

        time.sleep(0.01)
