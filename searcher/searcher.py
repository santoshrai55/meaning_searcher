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
            term = term.strip()
            term = term.lower()
            term = term.capitalize()
            print(f'this is the term: {term}')
            print("The term has been copied!")
            URL = f'https://www.dictionary.com/browse/{term}'

            print("Looking for the term ...")
            # ctrl-c is usually very fast but your program may execute faster
            time.sleep(.01)

            if term != "":
                page = requests.get(URL)
                print(page)
                time.sleep(0.01)
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

                def replacer(termbox):
                    try:
                        termbox = termbox.replace('etc.:', 'etc:\n')
                        termbox = termbox.replace('.', '\n')
                        termbox = termbox.replace('pronoun', 'PRONOUN: \n')
                        termbox = termbox.replace('noun', 'NOUN: \n')
                        termbox = termbox.replace(': ', ': \n')
                        termbox = termbox.replace('verbs', '\n\nVERBS: \n')
                        termbox = termbox.replace('verb ', '\n\nVERB: \n')
                        termbox = termbox.replace('SEE MORESEE LESS', ' ')
                    except:
                        termbox = termbox
                    return termbox

                meaning1 = replacer(terms)
                meaning2 = replacer(terms2)
                time.sleep(0.02)
                # print("--------RESULT--------")
                # print(final_term)
                # print("--------------------")
                result = {'term': term, 'meaning1': meaning1,
                          'meaning2': meaning2}
                return result

            else:
                print("The string is empty!")

        time.sleep(0.01)
