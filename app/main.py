from fastapi import FastAPI

from app.api.router import api_router

app = FastAPI(
    title="Py API",
    description="FastAPI 学习项目（阶段 1 脚手架）",
    version="0.1.0",
)

# 统一挂载业务路由。后续阶段继续在这里扩展（例如 auth、v2 路由等）。
app.include_router(api_router)


@app.get("/", tags=["system"], summary="根路径")
def root() -> dict[str, str]:
    """用于确认服务已启动。"""
    return {"message": "Hello World"}


@app.get("/health", tags=["system"], summary="健康检查")
def health() -> dict[str, str]:
    """给部署与监控系统使用的健康检查接口。"""
    return {"status": "ok"}


