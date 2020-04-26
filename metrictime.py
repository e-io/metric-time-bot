import datetime
import pytz

def current_metric_time():
    tz = pytz.timezone('Europe/Moscow')
    time = datetime.datetime.now(tz).time()

    # ms - milliseconds
    total_ms = 24 * 60 * 60 * 1000
    now_ms = ((time.hour * 60 + time.minute) * 60 + time.second) * 1000 + time.microsecond // 1000
    # mtime - metric time (= decimal time)
    mtime = round (now_ms / total_ms, 6)

    microdays = int(mtime * 10**6)
    centimilliday = microdays // 10
    milliday = centimilliday // 100
    centimilliday -= milliday * 100
    deciday = milliday // 100
    millidays = milliday
    microdays -= millidays * 1000
    milliday -= deciday * 100

    answer = f'Текущее московское время (GMT+3):\n' \
             f'- в метрических единицах: {millidays} миллидней и {microdays} микродней\n' \
             f'\tили просто {mtime}\n' \
             f'- в совмещенных единицах: {deciday}:{milliday}:{centimilliday}\n' \
             f'\t{deciday} метрических часов, {milliday} метрических минут, {centimilliday} метрических секунд\n' \
             f'- в вавилонских единицах: {time.hour}:{time.minute}:{time.second}'

    return answer
