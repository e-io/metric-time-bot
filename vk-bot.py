import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from datetime import datetime

import config

vk_session = vk_api.VkApi(token=config.vk_token)

session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print(f'Мы получили сообщение в {str(datetime.strftime(datetime.now(), "%Hh%Mm%Ss"))}' \
                   f' от пользователя id{event.user_id}')
            print('Текст сообщения: ' + str(event.text))
