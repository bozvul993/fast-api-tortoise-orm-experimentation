from fastapi.exceptions import HTTPException
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from config.database_config import data_base_config
from tortoise.contrib.fastapi import register_tortoise
from routers import category_api, keyword_api

app = FastAPI(title="Expense tracker")

register_tortoise(
    app,
    modules={"models": ["_models_"]},
    config=data_base_config,
    generate_schemas=True,
    add_exception_handlers=True,
)

app.include_router(category_api.router)
app.include_router(keyword_api.router)


@app.exception_handler(HTTPException)
async def unicorn_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
    )

