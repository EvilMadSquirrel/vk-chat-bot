from peewee import *

db = SqliteDatabase('vk_bot_db.db')


def get_state(user_id):
    print(user_id)
    return {
        'level': 0,
        'ID': 1,
    }


def set_state(state):
    print('saving state to the database')
    print(state)


def get_sections():
    print('getting sections from the database')
    return [0, 1, 2]


def get_products():
    print('getting products from the database')
    return [0, 1, 2]
