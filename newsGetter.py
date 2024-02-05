import requests
from datetime import datetime
from bs4 import BeautifulSoup

def get_news(date):
    # Format the data to YYYY-MM-DD
    date = datetime.strftime(date, '%Y-%m-%d')

    # Defining the url for Yahoo Finance with date parameter
    url = f'https://finance.yahoo.com/calendar/earnings?day={date}'

    # Making a request to the url and getting the response
    response = requests.get(url)

    # Parsing the response using beautiful soup 4 (which is a html parser)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Finding all the elements that contain the news
    headlines = soup.find_all('a', class_='Fw(600) C($linkColor)')

    # Extracting the text from the elements and storing it in a list
    news = [headline.text for headline in headlines]

    # Returning the list of news
    return news[0]