# -*- coding: utf-8 -*-
import re
import config
from telebot import TeleBot, types

bot = TeleBot(config.token)

@bot.message_handler(content_types=["text"])
def any_msg(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    # Склеиваем правильный ответ с неправильными
    # Создаем лист (массив) и записываем в него все элементы
    list_items = ['Карина', 'Какашка', 'Лупатая', 'Дзе пирог?']
    # Хорошенько перемешаем все элементы
    # Заполняем разметку перемешанными элементами
    for item in list_items:
        markup.add(item)
        
    return bot.send_message(message.chat.id, 'Верно!', reply_markup=markup)

if __name__ == '__main__':
     bot.polling(none_stop=True)
