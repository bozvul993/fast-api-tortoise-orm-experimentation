from tortoise.fields.data import DatetimeField
from tortoise.models import Model
from tortoise.fields import UUIDField, CharField
from tortoise.fields.relational import ManyToManyField, ManyToManyRelation
from tortoise.contrib.pydantic import pydantic_model_creator


class Category(Model):
    id = UUIDField(pk=True)
    name = CharField(max_length=255)
    description = CharField(max_length=255)
    keywords = ManyToManyField(
        "models.Keyword", related_name="categories", through="category_keywords"
    )
    created_on = DatetimeField(auto_now_add=True)
    updated_on = DatetimeField(auto_now=True)


Category_dto = pydantic_model_creator(Category, name="Category")

CategoryCreate_dto = pydantic_model_creator(
    Category, name="CategoryCreate", exclude=("id", "created_on", "updated_on"))
CategoryEdit_dto = pydantic_model_creator(
    Category, name="CategoryEdit", exclude=("created_on", "updated_on"))
