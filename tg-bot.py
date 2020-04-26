# @MetricTimeBot in telegram
# app is running on heroku.com

import telebot

import config
import metrictime

mybot = telebot.TeleBot(config.tg_token)


@mybot.message_handler(commands=['start'])
def start(message):
    answer_en = '''
            Welcome to metric time world! \n
            now, you can get \current_time in metric time units
            '''
    answer = '''Добро пожаловать в мир метрического времени!
                Выберите интересующую вас команду:
                \current_time - узнать текущее время в метрических единицах
                \start - повторить это сообщение'''
    mybot.send_message(message.chat.id, answer)


@mybot.message_handler(commands=['current_time'])
def current_time(message):
    mybot.send_message(message.chat.id, metrictime.current_metric_time())


@mybot.message_handler(content_types=['text'])
def reply(message):
    answer = '''Выберите одну из команд:
               \current_time - узнать текущее время в метрических единицах
               \start - стартовая информация'''
    mybot.send_message(message.chat.id, answer)


mybot.polling(none_stop=True)
