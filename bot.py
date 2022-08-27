import os

import vk_api
from dotenv import load_dotenv
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id

load_dotenv()

chat_token = os.getenv('TOKEN')
chat = vk_api.VkApi(token=chat_token)
longpoll = VkLongPoll(chat)


def write_message(receiver, message):
    chat.method('messages.send', {'peer_id': receiver, 'message': message, 'random_id': get_random_id()})


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        received_message = event.text
        sender = event.peer_id

        if received_message == 'Привет':
            write_message(sender, 'Добрый день!')
        elif received_message == 'Пока':
            write_message(sender, 'До встречи')
        else:
            write_message(sender, 'Я вас не понимаю...')