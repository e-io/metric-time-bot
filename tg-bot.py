# @MetricTimeBot in telegram
# app is running on heroku.com

import telebot

import config
import metrictime

mybot = telebot.TeleBot(config.tg_token)

@mybot.message_handler(commands=['start'])
def start(message):
    answer = '''
            Welcome to metric time world! \n
            now, you can get \current_time in metric time units
            '''
    mybot.send_message(message.chat.id, 'Welcome to metric time world!')

@mybot.message_handler(commands=['current_time'])
def current_time(message):
    mybot.send_message(message.chat.id, metrictime.current_metric_time())

@mybot.message_handler(content_types=['text'])
def reply(message):
    mybot.send_message(message.chat.id, 'Repeat, please')

mybot.polling(none_stop=True)