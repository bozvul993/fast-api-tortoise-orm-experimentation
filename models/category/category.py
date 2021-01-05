from tortoise.fields.data import DatetimeField
from tortoise.models import Model
from tortoise.fields import UUIDField, CharField
from tortoise.fields.relational import ManyToManyField


class Category(Model):
    id = UUIDField(pk=True)
    name = CharField(max_length=255)
    description = CharField(max_length=255)
    keywords = ManyToManyField(
        "models.Keyword", related_name="categories", through="category_keywords"
    )
    created_on = DatetimeField(auto_now_add=True)
    updated_on = DatetimeField(auto_now=True)
