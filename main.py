import os

from vkbottle import Keyboard, KeyboardButtonColor, Text, ABCRule
from vkbottle.bot import Bot, Message

from bot_db import db, get_sections, get_all_products, get_products, get_product
from dotenv import load_dotenv

load_dotenv()

chat_token = os.getenv('TOKEN')
bot = Bot(chat_token)
db.connect()

sections = get_sections()
all_products = get_all_products()


class SectionRule(ABCRule):
    async def check(self, event: Message):
        section_names = [section.name for section in sections]
        name = event.text.split()[-1]
        return name in section_names or name == "Продукты"


class StartRule(ABCRule):
    async def check(self, event: Message):
        text = event.text.split()[-1]
        return text in ['Старт', 'Разделы']


class ProductRule(ABCRule):
    async def check(self, event: Message):
        product_names = [product.name for product in all_products]
        name = event.text.split()[-1]
        return name in product_names


last_places = []


@bot.on.chat_message(SectionRule())
async def send_products(message: Message):
    section_name = message.text.split()[-1]
    if section_name == "Продукты":
        section_name = last_places.pop()
    last_places.append(section_name)
    products = get_products(section_name)
    keyboard = Keyboard()
    messages = []
    for product in products:
        messages.append((product.name, product.picture))
        keyboard.add(Text(product.name), color=KeyboardButtonColor.PRIMARY)
    keyboard.row()
    keyboard.add(Text("Разделы"), color=KeyboardButtonColor.NEGATIVE)
    for m in messages:
        await message.answer(message=m[0], attachment=m[1])
    await message.answer("Выберите продукт", keyboard=keyboard.get_json())


@bot.on.chat_message(StartRule())
async def send_sections(message: Message):
    keyboard = Keyboard()
    messages = []
    for section in sections:
        messages.append((section.name, section.picture))
        keyboard.add(Text(section.name), color=KeyboardButtonColor.PRIMARY)

    for m in messages:
        await message.answer(message=m[0], attachment=m[1])
    await message.answer("Выберите раздел", keyboard=keyboard.get_json())


@bot.on.chat_message(ProductRule())
async def send_product(message: Message):
    keyboard = Keyboard()
    keyboard.add(Text("Продукты"), color=KeyboardButtonColor.NEGATIVE)
    product_name = message.text.split()[-1]
    product = get_product(product_name)
    await message.answer(message=product.name, attachment=product.picture)
    await message.answer(message=product.description, keyboard=keyboard)


bot.run_forever()
