from tortoise.fields.data import DatetimeField
from tortoise.fields.relational import ManyToManyField
from tortoise.models import Model
from tortoise.fields import UUIDField, CharField
from tortoise.contrib.pydantic import pydantic_model_creator


class Expense(Model):
    id = UUIDField(pk=True)
    description = CharField(max_length=255)
    keywords = ManyToManyField(
         "models.Keyword", related_name="expenses", through="expenses_keywords"
    )
    created_on = DatetimeField(auto_now_add=True)
    updated_on = DatetimeField(auto_now=True)

Expense_dto = pydantic_model_creator(Expense, name="Expense", exclude=("created_on", "updated_on"))
ExpenseCreate_dto = pydantic_model_creator(Expense, name="ExpenseCreateCreate", exclude=("id","created_on", "updated_on"))