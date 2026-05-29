from pydantic import BaseModel, Field


class ItemBase(BaseModel):
    user: str = Field(..., min_length=1, max_length=10, description="user model")
    account: str = Field(..., min_length=5, max_length=20, description="account model")
    saving: float = Field(..., gt=0, description="saving model")


class ItemCreate(ItemBase):
    pass


class ItemUpdate(BaseModel):
    # name: str | None = Field(default=None, min_length=1, max_length=100)
    saving: float | None = Field(default=None, gt=0)

class ItemOut(ItemBase):
    id: int = Field(..., ge=1, description="generated id")

