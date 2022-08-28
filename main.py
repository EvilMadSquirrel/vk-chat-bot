import os

import vk_api
from bot import answer
from bot_db import db
from dotenv import load_dotenv
from vk_api.longpoll import VkLongPoll, VkEventType


load_dotenv()

chat_token = os.getenv('TOKEN')
chat = vk_api.VkApi(token=chat_token)
longpoll = VkLongPoll(chat)

if __name__ == '__main__':
    db.connect()
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
            answer(chat, event)

