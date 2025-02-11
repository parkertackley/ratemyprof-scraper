import requests
from bs4 import BeautifulSoup
import re

def scraper(url):

    try:
        # making a GET request
        req = requests.get(url)
        req.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("Cannot reach, request error: {e}")

    print(req)

    # parsing the html
    soup = BeautifulSoup(req.content, 'html.parser')

    # getting basic information
    professor = soup.find('h1', class_="NameTitle__NameWrapper-dowf0z-2")
    profNumbs4 = soup.find('a', class_="HeaderRateButton__StyledCompareProfessorButton-rxcxie-1")
    overall = soup.find('div', class_="RatingValue__Numerator-qw8sqy-2")
    wtalod = soup.find_all('div', class_='FeedbackItem__FeedbackNumber-uof32n-1')
    schoolName = soup.find('a', class_="TeacherTitles__TeacherSchoolLink-new3kl-3")
    professorNum = -1
    schoolNum = -1

    # Get id # of the professor
    if profNumbs4 and profNumbs4.has_attr('href'):
        href = profNumbs4['href']
        professorNum = re.findall(r'/compare/professors/(\d+)', href)

    # Get id # of the school
    if schoolName and schoolName.has_attr('href'):
        href = schoolName['href']
        schoolNum = re.findall(r'/school/(\d+)', href)

    # Get would take again and level of difficulty 
    wtalodList = []
    for entry in wtalod:
        wtalodList.append(entry.text)

    jsonEntry = {
        "school-number" : schoolNum,
        "id-number" : professorNum,
        "prof-name" : professor.text,
        "overall" : overall.text,
        "wta" : wtalodList[0],
        "lod" : wtalodList[1]
    }

    print(jsonEntry)
    return jsonEntry

# Alphonce
# scraper('https://www.ratemyprofessors.com/professor/17342')

# Hartlof
# scraper('https://www.ratemyprofessors.com/professor/2055417')

# Atri
# scraper('https://www.ratemyprofessors.com/professor/1434280')

# John Walsh (USC)
# scraper("https://www.ratemyprofessors.com/professor/2422438")

# scraper("https://www.ratemyprofessors.com/professor/1736675")
