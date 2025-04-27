from pydantic import BaseModel


class Contribution(BaseModel):
    user_id: int
    content: str
