from bs4 import BeautifulSoup
import pyperclip

import requests
import keyboard
import time

# import function from hindi.py
# this function searches hindi meaning of the provided term.
from . import functions


def searcher():

    hotkey = "shift + F1"

    while True:

        if keyboard.is_pressed(hotkey):
            # pyauto.typewrite('Hello world!')
            term = pyperclip.paste()
            term = term.strip()
            term = term.lower()
            term = term.capitalize()
            print(f'this is the term: {term}')
            print("The term has been copied!")
            # URL = f'https://www.dictionary.com/browse/{term}'

            print("Looking for the term ...")
            # ctrl-c is usually very fast but your program may execute faster
            time.sleep(.01)

            if term != "":
                # if ' ' in term:
                #     idiom = functions.idiomDefination(term)

                # else:
                #     idiom = " "
                english_meaning = functions.englishMeaning(term)
                hindi_meaning = functions.hindiMeaning(term)
                time.sleep(0.02)
                # print("--------RESULT--------")
                # print(final_term)
                # print("--------------------")

                result = {'term': term, 'english': english_meaning,
                          'hindi': hindi_meaning}
                return result
                # soup = BeautifulSoup(page.content, "html.parser")
                # terms = ''
                # try:
                #     terms = soup.find_all(
                #         "section", class_="css-109x55k e1hk9ate4")[0].text
                # except:
                #     terms = "meaning not found"
                # terms2 = ''

                # try:
                #     terms2 = soup.find_all(
                #         "section", class_="css-109x55k e1hk9ate4")[1].text
                # except:
                #     terms2 = ""

                # def replacer(termbox):
                #     try:
                #         termbox = termbox.replace('etc.:', 'etc\n')
                #         termbox = termbox.replace('etc.)', 'etc)')
                #         termbox = termbox.replace('adverb', 'ADVERB:\n')
                #         termbox = termbox.replace('adjective', 'ADJECTIVE:\n')
                #         termbox = termbox.replace('.', '\n')
                #         termbox = termbox.replace('pronoun', 'PRONOUN: \n')
                #         termbox = termbox.replace('noun', 'NOUN: \n')
                #         termbox = termbox.replace(': ', ': \n')
                #         termbox = termbox.replace('verbs', '\n\nVERBS: \n')
                #         termbox = termbox.replace('verb ', '\n\nVERB: \n')
                #         termbox = termbox.replace('SEE MORESEE LESS', ' ')
                #         termbox = termbox.replace('\n, ', ' ')
                #     except:
                #         termbox = termbox
                #     return termbox

                # meaning1 = replacer(terms)
                # meaning2 = replacer(terms2)

            else:
                print("The string is empty!")

        time.sleep(0.01)
