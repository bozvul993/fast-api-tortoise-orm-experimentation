from schemas.category import CategoryCreate_dto, Category_dto
from models.basic.uuid_list import UUIDList
from typing import List
from use_cases.category.category_use_cases import CategoryUseCases
from fastapi import APIRouter

router = APIRouter(
    prefix="/category",
    tags=["Category"]
)


@router.get('/list', response_model=List[Category_dto])
async def fetch_all():
    return await CategoryUseCases.get_all()


@router.get('/{category_id}', response_model=Category_dto)
async def fetch_one(category_id: str):
        category = await CategoryUseCases.get_one(category_id)
        return category
        

@router.post('/', response_model=Category_dto)
async def create(category: CategoryCreate_dto):
    return await CategoryUseCases.create(category)


@router.put('/add-keywords/{category_id}', response_model=Category_dto)
async def add_keywords(category_id: str, keyword_id_list: UUIDList):
    return await CategoryUseCases.add_keywords(category_id, keyword_id_list.ids) 

