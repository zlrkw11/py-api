# 阶段 1 手把手清单（你自己写代码版）

## 0) 先确认当前启动命令
在项目根目录执行：

```powershell
cd C:\Projects\py-api
.\.venv\Scripts\uvicorn.exe app.main:app --reload
```

看到 `/docs` 能打开即可。  
注意：现在点 `items` 接口会报 `NotImplementedError`，这是预期行为。

---

## 1) 先写 Schema（数据契约）
编辑 [schemas.py](/C:/Projects/py-api/app/modules/items/schemas.py:1)：

1. 在 `ItemBase` 补公共字段（建议 `name`、`description`、`price`）。
2. 在 `ItemCreate` 补“创建时必须字段”。
3. 在 `ItemUpdate` 把字段做成可选（支持更新部分字段）。
4. 在 `ItemOut` 增加 `id`。
5. 给关键字段加校验（长度、数值范围等）。

完成后重启/热更新，去 `/docs` 看请求体是否符合预期。

---

## 2) 再写 Store（内存数据）
编辑 [store.py](/C:/Projects/py-api/app/modules/items/store.py:1)：

1. 明确 `self.items` 的结构（建议 `dict[int, dict]`）。
2. 用 `self.next_id` 做自增 ID。
3. 可以补几个最基础方法（可选）：`insert` / `get` / `delete` / `list_all`。

目标：先让“存取数据”有统一位置，不要把数据操作散落在路由里。

---

## 3) 写 Service（业务逻辑）
编辑 [service.py](/C:/Projects/py-api/app/modules/items/service.py:1)：

1. 实现 `create_item`：生成 ID、写入 store、返回 `ItemOut`。
2. 实现 `list_items`：返回所有数据。
3. 实现 `get_item`：不存在时抛异常。
4. 实现 `update_item`：仅更新传入字段，不存在时抛异常。
5. 实现 `delete_item`：不存在时抛异常。

建议：定义你自己的业务异常（例如 `ItemNotFoundError`），让路由层统一转换成 404。

---

## 4) 写 Router（HTTP 层）
编辑 [router.py](/C:/Projects/py-api/app/modules/items/router.py:1)：

1. 保持路由函数只做“收参 + 调 service + 返回”。
2. 把业务异常转换为 `HTTPException(status_code=404)`。
3. 检查 5 个接口：
   - `POST /items`
   - `GET /items`
   - `GET /items/{item_id}`
   - `PUT /items/{item_id}`
   - `DELETE /items/{item_id}`

---

## 5) 人工验收（阶段 1）
打开 `http://127.0.0.1:8000/docs`，逐项验证：

1. 创建成功后能在列表中看到。
2. 查询详情正确。
3. 更新后字段变化正确。
4. 删除后查询不到。
5. 非法参数返回 422，不存在 ID 返回 404。

---

## 6) 完成标志
当以上都通过后，你就完成了阶段 1。  
下一步直接进阶段 2（pytest），把这 5 条行为写成自动化测试。

