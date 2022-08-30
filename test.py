import os

import pytest

from vkbottle import API
from dotenv import load_dotenv

load_dotenv()

chat_token = os.getenv("TOKEN")
vk_api = API(token=chat_token)


@pytest.mark.asyncio
async def test_get_profiles_via_token():
    profiles = await vk_api.users.get(user_id=1)
    assert profiles[0].last_name == "Дуров"
