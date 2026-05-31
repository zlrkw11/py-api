from fastapi import APIRouter

from app.models.schemas import ItemCreate, ItemOut, ItemUpdate
from app.services.service import item_service
from app.db.db import Item
from app.db.db import SessionDep

router = APIRouter(prefix="/items", tags=["items"])


@router.post("", response_model=ItemOut, status_code=201, summary="创建 item")
def create_item(payload: ItemCreate) -> ItemOut:
    return item_service.create_item(payload)


@router.get("", response_model=list[ItemOut], summary="获取 item 列表")
def list_items() -> list[ItemOut]:
    return item_service.list_items()


@router.get("/{item_id}", response_model=ItemOut, summary="获取单个 item")
def get_item(item_id: int) -> ItemOut:
    return item_service.get_item(item_id)


@router.put("/{item_id}", response_model=ItemOut, summary="更新 item")
def update_item(item_id: int, payload: ItemUpdate) -> ItemOut:
    return item_service.update_item(item_id, payload)


@router.delete("/{item_id}", status_code=204, summary="删除 item")
def delete_item(item_id: int) -> None:
    item_service.delete_item(item_id)

# db 操作
@router.post("/db/items", status_code=201, summary="创建item至db")
def db_create_item(item: Item, session: SessionDep) -> None:
    session.add(item)
    session.commit()
    session.refresh(item)