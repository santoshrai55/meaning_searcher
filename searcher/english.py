import requests
from bs4 import BeautifulSoup

# English Meaning Searcher


def englishMeaning(term):
    URL = f'https://www.dictionary.com/browse/{term}'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    terms = ''
    try:
        noun = soup.find_all(
            "div", class_="e1q3nk1v2")
        noun = [item.text for item in noun]
        noun = f'there are total {len(noun)} definations.'

        # noun = ' '.join(noun)
        # noun = noun.find_all('div', class_='css-69s207 e1hk9ate3')

        # terms = soup.find_all(
        #     "section", class_="css-109x55k e1hk9ate4")
        # meanings = [meaning.text for meaning in terms]
    except:
        noun = "noun not found"

    return noun


term = 'boss'
result = englishMeaning(term)
print(result)
