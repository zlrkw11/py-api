from pydantic import BaseModel, Field


class ItemBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=10, description="user model")
    saving: float = Field(..., gt=0, description="saving model")


class ItemCreate(ItemBase):
    pass


class ItemUpdate(BaseModel):
    # name: str | None = Field(default=None, min_length=1, max_length=100)
    name: str | None = Field(default=None, min_length=1, max_length=10)
    price: float | None = Field(default=None, gt=0)

class ItemOut(ItemBase):
    id: int = Field(..., ge=1, description="generated id")

