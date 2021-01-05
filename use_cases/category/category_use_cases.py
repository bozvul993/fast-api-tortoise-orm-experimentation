from typing import List
from schemas.category import Category, CategoryCreate_dto, Category_dto
from repositories.category_repository import CategoryRepository


class CategoryUseCases():

    @staticmethod
    async def get_all() -> List[Category_dto]:
        all_categories = await CategoryRepository.get_all()
        return all_categories

    @staticmethod
    async def get_one(id: str) -> Category_dto:
        category_orm = await CategoryRepository.get_one(id)
        category = await Category_dto.from_tortoise_orm(category_orm)
        return category

    @staticmethod
    async def create(category: CategoryCreate_dto) -> Category_dto:
        category_orm = await CategoryRepository.create(category)
        return await Category_dto.from_tortoise_orm(category_orm)

    @staticmethod
    async def add_keywords(category_id: str, keyword_id_list: List[str]):
        await CategoryRepository.add_keywords(category_id, keyword_id_list)
