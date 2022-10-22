import logging
import requests
from bs4 import BeautifulSoup


response = ''
source_url='https://allrivers.info/gauge/oka-ryazan/waterlevel'


def check_level():

    res = requests.get(source_url)
    soup = BeautifulSoup(res.content, 'html.parser')
    logging.info(f"Parsing html page")

    water_class = soup.find('span', {'class': 'gauge-value'})
    water_level = water_class.text.strip()
    logging.info(f"get water level {water_level}")

    delta_class = soup.find('span', {'class': 'font-bold'})
    delta_level = delta_class.text.strip()
    logging.info(f"get delta {delta_level}")

    response = 'Уровень воды в реке: ' + water_level + ' см, ' + ' за последние сутки изменился на ' + delta_level + ' см.'

    return response
