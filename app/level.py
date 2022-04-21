import logging
import requests
from bs4 import BeautifulSoup


response = ''

def check_level():

    res = requests.get(
        'https://allrivers.info/gauge/oka-ryazan')
    soup = BeautifulSoup(res.content, 'html.parser')

    water_class = soup.find('span', {'class': 'gauge-value'})
    water_level = water_class.text.strip()
    logging.info(f"уровень воды {water_level}")

    delta_class = soup.find('span', {'class': 'font-bold'})
    delta_level = delta_class.text.strip()
    logging.info(f"дельта {delta_level}")

    response = 'Уровень воды в реке: ' + water_level + ' см, ' + ' за последние сутки изменился на ' + delta_level + ' см.'

    return response
