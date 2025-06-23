import requests
from bs4 import BeautifulSoup

def scrape_college_info():
    url = "https://www.collegesintamilnadu.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.get_text()
