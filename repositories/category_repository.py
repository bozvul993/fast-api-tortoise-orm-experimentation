from models.keyword import Keyword
from typing import List

from schemas.category import Category_dto, CategoryCreate_dto
from util.exceptions.not_found import NotFoundHTTP
from models.category.category import Category
from tortoise.query_utils import Q


class CategoryRepository():

    @staticmethod
    async def get_all() -> List[Category_dto]:
        return await Category_dto.from_queryset(Category.all())

    @staticmethod
    async def get_one(id: str) -> Category:
        category_orm = await Category.get_or_none(id=id).prefetch_related('keywords')
        if (category_orm is None):
            raise NotFoundHTTP('Category')
        return category_orm

    @staticmethod
    async def create(category: CategoryCreate_dto) -> Category_dto:
        return await Category.create(**category.dict(exclude_unset=True))

    @classmethod
    async def add_keywords(cls, category_id: str, keyword_id_list: List[str]):
        keywords_query_set = await Keyword.filter(Q(id__in=keyword_id_list))
        category = await Category.get(id=category_id)
        await category.keywords.add(*keywords_query_set)
