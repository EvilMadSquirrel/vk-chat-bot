import os

import vk_api
from bot import answer
from bot_db import db, User, Section, Product
from dotenv import load_dotenv
from vk_api.longpoll import VkLongPoll, VkEventType


load_dotenv()

chat_token = os.getenv('TOKEN')
chat = vk_api.VkApi(token=chat_token)
longpoll = VkLongPoll(chat)

if __name__ == '__main__':
    db.connect()
    User.create_table()
    Section.create_table()
    Product.create_table()
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
            answer(chat, event)

