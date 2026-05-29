from app.schemas import ItemCreate, ItemOut, ItemUpdate
from .store import ItemMemoryStore
from fastapi import HTTPException


class ItemService:
    def __init__(self, store: ItemMemoryStore) -> None:
        self.store = store

    def create_item(self, payload: ItemCreate) -> ItemOut:
        raise NotImplementedError("")

    def list_items(self) -> list[ItemOut]:
        data = self.store.get_all()
        res = []
        if data is None:
            raise HTTPException(status_code=404, detail="no products found")
        for item in data:
            if item is None:
                raise HTTPException(status_code=404, detail="item not found")
        
            res.append(ItemOut(item))
        return res 
            

    def get_item(self, item_id: int) -> ItemOut:
        data = self.store.get(item_id)
        if data is None:
            raise HTTPException(status_code=404, detail="product not found")
        return ItemOut(id=item_id, **data)
        

    def update_item(self, item_id: int, payload: ItemUpdate) -> ItemOut:
        raise NotImplementedError("")

    def delete_item(self, item_id: int) -> None:
        raise NotImplementedError("")


# 阶段 1 先用单例服务，后续阶段会切到数据库 session 注入。
item_service = ItemService(store=ItemMemoryStore())

