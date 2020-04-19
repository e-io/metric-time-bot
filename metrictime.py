import datetime

def current_metric_time():
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
    answer = f'Metric time now: {deciday}:{milliday}:{centimilliday}\n' \
            f'or simply {mtime}\n' \
            f'Babylonian time: {time.hour}:{time.minute}:{time.second}'
    return answer
