import telebot
import logging
import os

from libs.logs import log_date, log_struct
from level import check_level
from telebot import types

log_level = os.getenv("LOG_LEVEL", "INFO")
logging.basicConfig(format=log_struct, datefmt=log_date, level=log_level)

token = os.environ['TOKEN']

# Init bot
bot = telebot.TeleBot(token)
@bot.message_handler(commands=["start"])
def start(m, res=False):
        # Add button
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Уровень")
        markup.add(item1)
        bot.send_message(m.chat.id, 'Нажми: \n"Уровень" \n Для получения текущего уровня воды в реке Ока на территории Рязани',  reply_markup=markup)
# Get message from user
@bot.message_handler(content_types=["text"])
def handle_text(message):
    # If user tap button, return water level from level.py
    if message.text.strip() == 'Уровень':
        answer = check_level()
    logging.warning(f"send message: {answer}")
    bot.send_message(message.chat.id, answer)

# Run
logging.warning("Running bot")
bot.polling(none_stop=True, interval=0)
