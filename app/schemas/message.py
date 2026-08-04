from datetime import datetime

from pydantic import BaseModel, ConfigDict


class MessageCreate(BaseModel):
    content: str


class MessageResponse(BaseModel):
    id: int
    sender: str
    content: str
    timestamp: datetime

    model_config = ConfigDict(
        from_attributes=True,
    )