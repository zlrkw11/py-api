from app.modules.items.schemas import ItemCreate, ItemOut, ItemUpdate
from app.modules.items.store import ItemMemoryStore


class ItemService:
    """
    业务服务层：
    - 处理数据组装、业务规则、异常判断。
    - 路由层只负责参数接收和响应返回，尽量不写业务细节。
    """

    def __init__(self, store: ItemMemoryStore) -> None:
        self.store = store

    def create_item(self, payload: ItemCreate) -> ItemOut:
        # TODO: 1) 生成 item_id 2) 写入内存 3) 返回 ItemOut
        raise NotImplementedError("TODO: 实现 create_item")

    def list_items(self) -> list[ItemOut]:
        # TODO: 返回所有 item 列表
        raise NotImplementedError("TODO: 实现 list_items")

    def get_item(self, item_id: int) -> ItemOut:
        # TODO: 查找 item，不存在时抛出业务异常（供路由层转成 404）
        raise NotImplementedError("TODO: 实现 get_item")

    def update_item(self, item_id: int, payload: ItemUpdate) -> ItemOut:
        # TODO: 支持更新指定 item，不存在时抛出业务异常
        raise NotImplementedError("TODO: 实现 update_item")

    def delete_item(self, item_id: int) -> None:
        # TODO: 删除指定 item，不存在时抛出业务异常
        raise NotImplementedError("TODO: 实现 delete_item")


# 阶段 1 先用单例服务，后续阶段会切到数据库 session 注入。
item_service = ItemService(store=ItemMemoryStore())

