from tortoise.contrib.pydantic import pydantic_model_creator

from models.category import Category

Category_dto = pydantic_model_creator(Category, name="Category")
CategoryCreate_dto = pydantic_model_creator(
    Category, name="CategoryCreate", exclude=("id", "created_on", "updated_on"))
CategoryEdit_dto = pydantic_model_creator(
    Category, name="CategoryEdit", exclude=("created_on", "updated_on"))