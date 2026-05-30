from app.schemas import ItemCreate, ItemOut, ItemUpdate
from .store import ItemMemoryStore
from fastapi import HTTPException


class ItemService:
    def __init__(self, store: ItemMemoryStore) -> None:
        self.store = store

    def create_item(self, payload: ItemCreate) -> ItemOut:
        item_id = self.store.allocate_id()
        data = payload.model_dump()
        self.store.insert(item_id, data)
        return ItemOut(id=item_id, **data)

    def list_items(self) -> list[ItemOut]:
        rows = self.store.get_all()
        return [ItemOut(id=item_id, **data) for item_id, data in rows]

    def get_item(self, item_id: int) -> ItemOut:
        data = self.store.get(item_id)
        if data is None:
            raise HTTPException(status_code=404, detail="product not found")
        return ItemOut(id=item_id, **data)
        

    def update_item(self, item_id: int, payload: ItemUpdate) -> ItemOut:
        patch = payload.model_dump(exclude_none=True)
        updated = self.store.update(item_id, patch)
        if updated is None:
            raise HTTPException(status_code=404, detail="product not found")
        return ItemOut(id=item_id, **updated)

    def delete_item(self, item_id: int) -> None:
        deleted = self.store.delete(item_id)
        if not deleted:
            raise HTTPException(status_code=404, detail="product not found")

item_service = ItemService(store=ItemMemoryStore())
