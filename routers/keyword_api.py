from models.keyword import Keyword_dto, KeywordCreate_dto
from typing import List
from use_cases.keyword.keyword_use_cases import KeywordUseCases
from fastapi import APIRouter

router = APIRouter(
    prefix="/keyword",
    tags=["Keyword"]
)


@router.get('/list', response_model=List[Keyword_dto])
async def fetch_all():
    return await KeywordUseCases.get_all()


@router.get('/{keyword_id}', response_model=Keyword_dto)
async def fetch_one(keyword_id: str):
        keyword = await KeywordUseCases.get_one(keyword_id)
        return keyword

@router.post('/', response_model=Keyword_dto)
async def create(keyword: KeywordCreate_dto):
    return await KeywordUseCases.create(keyword)    