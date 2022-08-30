from peewee import *

db = SqliteDatabase("vk_bot_db.db")


class BaseModel(Model):
    class Meta:
        database = db


class Section(BaseModel):
    name = CharField(null=False)
    picture = CharField(null=True)


class Product(BaseModel):
    name = CharField(max_length=250, null=False)
    description = CharField(null=False)
    picture = CharField(null=True)
    section = ForeignKeyField(Section, backref="products")


def get_sections():
    return Section.select()


def get_all_products():
    return Product.select()


def get_products(section_name):
    return Product.select().where(
        Product.section == Section.get(Section.name == section_name)
    )


def get_product(product_name):
    return Product.get(Product.name == product_name)
