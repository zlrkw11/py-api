from typing import Any
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

def convertData(id: str, item: BaseModel) -> dict[str, Any]:
    jsonData = jsonable_encoder(item)
    return {"id": id, **jsonData}
    
