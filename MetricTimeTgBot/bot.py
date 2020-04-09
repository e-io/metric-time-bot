# @MetricTimeBot
# app is running on pythonanywhere.com

import telebot
import config

mybot = telebot.TeleBot(config.TOKEN)

@mybot.message_handler(commands=['start'])
def start(message):
    mybot.send_message(message.chat.id, 'Welcome to metric time world!')

@mybot.message_handler(content_types=['text'])
def reply(message):
    mybot.send_message(message.chat.id, 'Repeat, please')

mybot.polling(none_stop=True)

