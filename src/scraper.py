import requests
from bs4 import BeautifulSoup

def scraper(url):
    # making a GET request
    req = requests.get(url)

    print(req)

    # parsing the html
    soup = BeautifulSoup(req.content, 'html.parser')

    professor = soup.find('h1', class_="NameTitle__NameWrapper-dowf0z-2")
    overall = soup.find('div', class_="RatingValue__Numerator-qw8sqy-2")
    wtalod = soup.find_all('div', class_='FeedbackItem__FeedbackNumber-uof32n-1')

    wtalodList = []
    for entry in wtalod:
        wtalodList.append(entry.text)

    print(professor.text + "\n" +
          overall.text + "\n" +
          "Would take again: " + wtalodList[0] + "\n" +
          "Level of Difficulty: " + wtalodList[1])

# Alphonce
scraper('https://www.ratemyprofessors.com/professor/17342')

# Hartlof
# scraper('https://www.ratemyprofessors.com/professor/2055417')

# Atri
# scraper('https://www.ratemyprofessors.com/professor/1434280')
