# @MetricTimeBot
# app is running on pythonanywhere.com

import telebot
import config
import datetime

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
    time = datetime.datetime.now().time()
    # ms - milliseconds
    total_ms = 24 * 60 * 60 * 1000
    now_ms = ((time.hour * 60 + time.minute) * 60 + time.second) * 1000 + time.microsecond // 1000
    # mtime - metric time (= decimal time)
    mtime = now_ms / total_ms
    centimilliday = int(round(mtime, 5) * 100000)
    milliday = centimilliday // 100
    centimilliday = centimilliday - milliday * 100
    deciday = milliday // 100
    milliday = milliday - deciday * 100
    mtime = round(mtime, 5)
    answer = f'''
            Metric time now: {deciday}:{milliday}:{centimilliday} \n
            or simply {mtime}. \n
            Babylonian time: {time.hour}:{time.minute}:{time.second}
            '''
    mybot.send_message(message.chat.id, answer)

@mybot.message_handler(content_types=['text'])
def reply(message):
    mybot.send_message(message.chat.id, 'Repeat, please')

mybot.polling(none_stop=True)

