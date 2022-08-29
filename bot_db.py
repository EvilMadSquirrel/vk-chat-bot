from peewee import *

db = SqliteDatabase('vk_bot_db.db')


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    level = IntegerField(default=0)
    state = IntegerField(default=0)
    user_id = IntegerField(null=False)


class Section(BaseModel):
    name = CharField(null=False)


class Product(BaseModel):
    name = CharField(max_length=250, null=False)
    description = CharField(null=False)
    section = ForeignKeyField(Section, backref='products')


def get_state(user_id):
    try:
        user = User.get(User.user_id == user_id)
    except DoesNotExist:
        user = User.create(user_id=user_id, level=0, state=0)

    return {
        'level': user.level,
        'state': user.state,
    }


def set_state(user_id, state):
    user = User.get(User.user_id == user_id)
    user.level = state['level']
    user.state = state['state']
    user.save()


def get_sections():
    return Section.select()


def get_products(section_id):
    return Product.select().where(Product.section == section_id)
