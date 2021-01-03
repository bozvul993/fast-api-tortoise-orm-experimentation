from typing import List
from util.exceptions.not_found import NotFoundHTTP
from models.keyword import Keyword, Keyword_dto, KeywordCreate_dto


class KeywordRepository():

    @staticmethod
    async def get_all() -> List[Keyword_dto]:
        return await Keyword_dto.from_queryset(Keyword.all())

    @staticmethod
    async def get_one(id: str) -> Keyword_dto:
            keyword = await Keyword.get_or_none(id=id).prefetch_related('categories')
            if (keyword is None):
                raise NotFoundHTTP('Keyword')
            return keyword

    @staticmethod
    async def create(keyword: KeywordCreate_dto) -> Keyword_dto:
        keyword_obj = await Keyword.create(**keyword.dict(exclude_unset=True))
        return await Keyword_dto.from_tortoise_orm(keyword_obj)