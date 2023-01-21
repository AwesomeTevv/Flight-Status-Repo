from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.flysafair.co.za/travel-tools/flight-status').text

soup = BeautifulSoup(html_text, 'lxml')

flights = soup.find_all('tbody')
