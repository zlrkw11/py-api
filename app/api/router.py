from fastapi import APIRouter

from app.modules.items.router import router as items_router

# 统一管理所有业务子路由，main.py 只 include 这一个对象。
api_router = APIRouter()
api_router.include_router(items_router)

