from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.flysafair.co.za/travel-tools/flight-status').text

soup = BeautifulSoup(html_text, 'lxml')

flights = soup.find_all('tr')

for flight in flights:
    flight_details = flight.find_all('td')
    
    flight_num = flight_details[0].text
    origin = flight_details[1].text
    dest = flight_details[2].text
    depart_time = flight_details[3].text
    arrival_time = flight_details[4].text
    status = flight_details[5].text
    
    print(f'Flight Number: {flight_num}')
    print(f'From: {origin}')
    print(f'To: {dest}')
    print(f'Depart Time: {depart_time}')
    print(f'Arrival Time: {arrival_time}')
    print(f'Status: {status}')
    print('-------------------------------------------')
