# FastAPI 学习计划（5 个阶段）

## 使用方式
- 每个阶段先完成「实作任务」，再做「验收标准」。
- 阶段内代码都基于当前仓库 `C:\Projects\py-api`。
- 运行命令统一在项目根目录执行。

---

## 阶段 1：FastAPI routes + Pydantic schemas + in-memory data
### 目标
- 会写 CRUD 路由。
- 会用 Pydantic 做请求/响应模型校验。
- 先用内存数据结构（`list` / `dict`）跑通业务流程。

### 实作任务
1. 在 `app/main.py` 建立 `items` 资源：
   - `POST /items`
   - `GET /items`
   - `GET /items/{item_id}`
   - `PUT /items/{item_id}`
   - `DELETE /items/{item_id}`
2. 定义 Pydantic 模型（建议放 `app/schemas.py`）：
   - `ItemCreate`
   - `ItemUpdate`
   - `ItemOut`
3. 用内存 `dict[int, ItemOut]` 做数据存储。
4. 统一错误返回（找不到资源时返回 404）。

### 验收标准
- `uvicorn app.main:app --reload` 可以启动。
- `/docs` 中 5 个接口都可调用。
- 参数非法时返回 422，ID 不存在返回 404。

### 建议时长
- 2-3 天

---

## 阶段 2：pytest 测 API
### 目标
- 会写 API 自动化测试，覆盖核心路径和错误路径。

### 实作任务
1. 安装测试依赖：`pytest`、`httpx`（或 `fastapi[test]`）。
2. 新建 `tests/test_items.py`，使用 `fastapi.testclient.TestClient`。
3. 覆盖测试：
   - 创建成功
   - 查询列表/详情成功
   - 更新成功
   - 删除成功
   - 404 / 422 场景
4. 为内存数据增加测试隔离（每个测试清理状态）。

### 验收标准
- `pytest -q` 全绿。
- 关键业务路径都有测试，不依赖手工点 `/docs`。

### 建议时长
- 2 天

---

## 阶段 3：SQLite 数据库
### 目标
- 从内存数据迁移到 SQLite，理解 ORM 基础。

### 实作任务
1. 选择 ORM（推荐 SQLAlchemy 2.x + `sqlite`）。
2. 新建模块：
   - `app/db.py`（engine, session）
   - `app/models.py`（ORM 模型）
   - `app/crud.py`（数据库操作）
3. 将阶段 1 的路由改为数据库读写。
4. 数据库文件使用 `sqlite:///./app.db`。
5. 保留 Pydantic 响应模型，避免直接暴露 ORM 对象。

### 验收标准
- 重启服务后数据仍存在（不再丢失）。
- 所有阶段 2 测试通过（按需调整 fixture）。

### 建议时长
- 3-4 天

---

## 阶段 4：JWT auth
### 目标
- 为受保护接口加登录认证，理解 access token 流程。

### 实作任务
1. 实现用户模型（最少字段：`username`、`hashed_password`）。
2. 增加接口：
   - `POST /auth/register`
   - `POST /auth/login`（返回 JWT access token）
3. 对 `items` 写操作接口加认证（POST/PUT/DELETE）。
4. 使用 `Depends` + `OAuth2PasswordBearer` 获取当前用户。
5. 增加 token 过期处理与 401 返回。

### 验收标准
- 未带 token 调用受保护接口返回 401。
- 有效 token 可正常增删改。
- 登录失败场景（密码错误、用户不存在）覆盖测试。

### 建议时长
- 3-4 天

---

## 阶段 5：Docker / deployment 设计
### 目标
- 会把服务容器化，并具备基础部署思路。

### 实作任务
1. 编写 `Dockerfile`（Python slim 基础镜像）。
2. 编写 `docker-compose.yml`（先单服务；可后续加反向代理）。
3. 配置环境变量（如 `SECRET_KEY`、`DATABASE_URL`）。
4. 准备生产启动命令（例如 `uvicorn app.main:app --host 0.0.0.0 --port 8000`）。
5. 输出一页部署说明（本地运行、构建、启动、健康检查）。

### 验收标准
- `docker compose up --build` 后接口可访问。
- 容器重启后服务可恢复。
- 有最小化部署文档可供复现。

### 建议时长
- 2-3 天

---

## 最终里程碑
- 你将得到一个包含 CRUD、测试、数据库、认证、容器化的 FastAPI 项目骨架。
- 每完成一个阶段就打一个 git commit，便于回滚和复盘。
