from vk_api.utils import get_random_id

from bot_db import get_state


def answer(chat, event):
    receiver = event.peer_id
    state = get_state(receiver)

    message = f'level: {state["level"]} ID: {state["state"]}'
    chat.method('messages.send', {'peer_id': receiver, 'message': message, 'random_id': get_random_id()})
