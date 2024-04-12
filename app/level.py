import logging
import requests
import re
import os
from bs4 import BeautifulSoup


response = ''
source_url = os.environ['URL']

if 'URL' not in os.environ:
    logging.error("Переменная окружения URL не установлена")


def check_level():
    logging.info(f"Парсим страницу: {source_url}")

    try:
        res = requests.get(source_url)
        res.raise_for_status()
        soup = BeautifulSoup(res.content, 'html.parser')
    except requests.RequestException as e:
        logging.error(f"Ошибка выполнения запроса: {e}")
        return
    except Exception as e:
        logging.error(f"Ошибка парсинга HTML: {e}")
        return

    # Регулярное выражение для поиска строки с заданным шаблоном
    level_pattern = r"уровень воды в реке Ока по данным гидропоста.*?(\d+) cм над нулем поста"
    delta_pattern = r"на (\d+) см"

    # Поиск совпадений в тексте
    level_match = re.search(level_pattern, soup.text, re.IGNORECASE)
    delta_match = re.search(delta_pattern, soup.text, re.IGNORECASE)

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

    response = f'Уровень воды в реке: {water_level} см, за последние сутки изменился на {delta_level} см.'

    return response
