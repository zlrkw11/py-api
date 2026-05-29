from typing import Any

class ItemMemoryStore:
    
    def __init__(self) -> None:
        self.items: dict[int, dict[str, Any]] = {}
        self.next_id = 1
        
    def allocate_id(self) -> int:
        item_id = self.next_id
        self.next_id += 1
        return item_id
    
    def insert(self, item_id: int, data: dict[str, Any]) -> None:
        self.items[item_id] = data.copy()

    def get_all(self) -> list[dict[str, Any]]:
        return [item.copy() for item in self.items.values()]

    def get(self, item_id: int) -> dict[str, Any] | None:
        data = self.items.get(item_id)
        return data.copy() if data is not None else None

    def update(self, item_id: int, patch: dict[str, Any]) -> dict[str, Any] | None:
        current = self.items.get(item_id)
        if current is None:
            return None
        current.update(patch)
        return current.copy()

    def delete(self, item_id: int) -> bool:
        return self.items.pop(item_id, None) is not None