import telebot
import logging
import os
import time
from libs.logs import log_date, log_struct
from level import check_level
from telebot import types

log_level = os.getenv("LOG_LEVEL", "INFO")
logging.basicConfig(format=log_struct, datefmt=log_date, level=log_level)

token = os.getenv("TOKEN")

if not token:
    logging.error("Переменная окружения TOKEN не установлена")

bot = telebot.TeleBot(token)


def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Уровень")
    markup.add(item1)
    bot.send_message(
        message.chat.id,
        'Нажми "Уровень" для получения текущего уровня воды в реке Ока на территории Рязани',
        reply_markup=markup,
    )


@bot.message_handler(commands=["start"])
def handle_start(message):
    start(message)


@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.strip() == "Уровень":
        answer = check_level()
        user_first_name = str(message.chat.first_name)
        user_id = str(message.chat.id)
        logging.warning(
            f"Отправлено сообщение: {answer} пользователю:  {user_first_name} - {user_id} "
        )
        bot.send_message(message.chat.id, answer)


def main():
    while True:
        try:
            logging.warning("Запуск бота")
            bot.polling(none_stop=True, interval=0, timeout=90)
        except Exception as e:
            logging.error(f"Ошибка: {e}")
            time.sleep(5)


if __name__ == "__main__":
    main()
