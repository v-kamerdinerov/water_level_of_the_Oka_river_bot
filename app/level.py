import logging
import requests
import re
from bs4 import BeautifulSoup


response = ''
source_url='https://allrivers.info/gauge/oka-ryazan/waterlevel'


def check_level():

    res = requests.get(source_url)
    soup = BeautifulSoup(res.content, 'html.parser')
    logging.info(f"Parsing html page")

    text = soup.text

    # Регулярное выражение для поиска строки с заданным шаблоном
    level_pattern = r"уровень воды в реке Ока по данным гидропоста.*?(\d+) cм над нулем поста"
    delta_pattern = r"повысился на (\d+) см"

    # Поиск совпадений в тексте
    level_match = re.search(level_pattern, text, re.IGNORECASE)
    delta_match = re.search(delta_pattern, text, re.IGNORECASE)

    # Если совпадение найдено, извлекаем число
    if level_match:
        water_level = level_match.group(1)
        logging.info(f"get water level {water_level}")
    else:
        logging.error("Строка уровня не найдена")

    if delta_match:
        delta_level = delta_match.group(1)
        logging.info(f"get delta {delta_level}")
    else:
        logging.error("Строка дельты не найдена")

    response = 'Уровень воды в реке: ' + water_level + ' см, ' + ' за последние сутки изменился на ' + delta_level + ' см.'

    return response
