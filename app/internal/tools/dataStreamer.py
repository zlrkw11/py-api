# json streaming (line by line)
from pydantic import BaseModel

class Item(BaseModel):
    firstname: str
    lastname: str | None
    
items = [
    Item(firstname="ray", lastname="zhao"),
    Item(firstname="john", lastname="doe"),
]

