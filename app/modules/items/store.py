class ItemMemoryStore:
    """
    in-memory 数据仓库（阶段 1 使用）。

    设计说明：
    - 用 dict 存储条目，key 是 item_id，value 是字典或模型数据。
    - 用 next_id 模拟数据库自增主键。
    """

    def __init__(self) -> None:
        # TODO: 你来定义数据结构（建议 dict[int, dict]）。
        self.items = {}
        self.next_id = 1

