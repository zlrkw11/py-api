from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

class RouteException(Exception):
    def __init__(self, name:str):
        self.name = name 

def register_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(RouteException)
    async def custom_exception_handler(request: Request, exc: RouteException):
        return JSONResponse(
            status_code=418,
            content={"message": f"{exc.name} raised an exception"},
        )