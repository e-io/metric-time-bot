#now bot works in group https://vk.com/thesideoflight

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from datetime import datetime

import config
import metrictime

vk_session = vk_api.VkApi(token=config.vk_token)

session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)
counter = 0

while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print(f'Мы получили сообщение в {str(datetime.strftime(datetime.now(), "%HH%MM%SS"))}' \
                  f' от пользователя id{event.user_id}')
            print(f'Текст сообщения: {str(event.text)}')
            if event.from_user and not event.from_me:
                counter = event.message_id + 1
                vk_session.method('messages.send', {'user_id': event.user_id,
                                                'message': metrictime.current_metric_time(),
                                                'random_id': counter})