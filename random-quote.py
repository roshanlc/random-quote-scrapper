
# Random-quote-scrapper
# It selects first quote from the randomly selected topic section of brainyquote.com

import  requests as req
from bs4 import BeautifulSoup as bs
import random

def extract(xyz): # function to extract quote and author name
    x = str(xyz).split('>')
    y = str(x[1]).split('<')
    z = y[0]
    return z

def printl(): #function to print lines
    print("_____________________________________________________________")
    print()

qSection = ["age-quotes","experience-quotes","alone-quotes","religion-quotes","famous-quotes","communication-quotes",
"computers-section","cool-quotes","courage-quotes","imagination-quotes","independence-quotes","inspirational-quotes",
"intelligence-quotes","moving-on-quotes","music-quotes","nature-quotes","parenting-quotes",
"patience-quotes","peace-quotes","poetry-quotes","politics-quotes","positive-quotes","relationship-quotes",
"religion-quotes"]  # a bunch of quotes section to select from

randomNum = random.randint(0,(len(qSection)-1))
url = 'https://www.brainyquote.com/topics/' + qSection[randomNum]
try:
    page=req.get(url)
    soup = bs(page.content,'html.parser')
    detail1 = soup.find('a',attrs={"title": "view quote"}) #quote
    detail2 = soup.find('a',attrs={"title": "view author"})   #person who said the quote/author
    quote = extract(detail1)
    author = extract(detail2)
    printl()
    print(quote, " - ", author)
    printl()
except:
    print("Error occured!")
    print("Error code :" ,page.status_code)
