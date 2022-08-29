import enum
from vk_api.utils import get_random_id
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

from bot_db import get_sections, get_products, get_product, get_all_products


def send_message(chat, receiver, message='', keyboard=None, attachment=None):
    key = None
    if keyboard:
        key = keyboard.get_keyboard()
    chat.method('messages.send', {
            'peer_id': receiver,
            'message': message,
            'random_id': get_random_id(),
            'keyboard': key,
            'attachment': attachment
        })


def answer(chat, event):
    from_button = event.message
    receiver = event.peer_id
    sections = get_sections()
    section_names = [section.name for section in sections]
    products = get_all_products()
    product_names = [product.name for product in products]
    keyboard = VkKeyboard(one_time=True)

    if from_button in section_names:
        section_products = get_products(from_button)
        for product in section_products:
            send_message(chat=chat, receiver=receiver, message=product.name, attachment=product.picture)

        section_products_names = [product.name for product in section_products]

        for name in section_products_names:
            keyboard.add_button(name, color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Назад', color=VkKeyboardColor.NEGATIVE)

        send_message(chat=chat, receiver=receiver, message='Выберите раздел', keyboard=keyboard)

    elif from_button in product_names:
        pass
    else:
        for section in sections:
            send_message(chat=chat, receiver=receiver, message=section.name, attachment=section.picture)

        for name in section_names:
            keyboard.add_button(name, color=VkKeyboardColor.PRIMARY)

        send_message(chat=chat, receiver=receiver, message='Выберите раздел', keyboard=keyboard)




