from typing import List
from models.keyword import Keyword_dto, KeywordCreate_dto
from repositories.keyword_repository import KeywordRepository


class KeywordUseCases():

    @staticmethod
    async def get_all() -> List[Keyword_dto]:
        all_keywords = await KeywordRepository.get_all()
        return all_keywords

    @staticmethod
    async def get_one(id: str) -> Keyword_dto:
        keyword_orm = await KeywordRepository.get_one(id)
        keyword = await Keyword_dto.from_tortoise_orm(keyword_orm)
        return keyword

    @staticmethod
    async def create(keyword: KeywordCreate_dto) -> Keyword_dto:
        keyword = await KeywordRepository.create(keyword)
        return keyword