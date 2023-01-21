from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.flysafair.co.za/travel-tools/flight-status').text

soup = BeautifulSoup(html_text, 'lxml')

flight_list = soup.find('tbody')
flights = flight_list.find_all('tr')

for flight in flights:
    print(flight)
