from models.expense import Expense
from models.category import Category
from tortoise.fields.data import DatetimeField
from tortoise.fields.relational import ManyToManyRelation
from tortoise.models import Model
from tortoise.fields import UUIDField, CharField
from tortoise.contrib.pydantic import pydantic_model_creator


class Keyword(Model):
    id = UUIDField(pk=True)
    name = CharField(max_length=255)
    description = CharField(max_length=255)
    categories: ManyToManyRelation[Category]
    expenses: ManyToManyRelation[Expense]
    created_on = DatetimeField(auto_now_add=True)
    updated_on = DatetimeField(auto_now=True)


Keyword_dto = pydantic_model_creator(Keyword)
KeywordCreate_dto = pydantic_model_creator(Keyword, name="KeywordCreate", exclude=("id","created_on", "updated_on"))