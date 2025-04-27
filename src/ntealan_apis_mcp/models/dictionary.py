from pydantic import BaseModel


class Dictionary(BaseModel):
    dictionary_id: str | None = None
    name: str | None = None
    description: str | None = None
    created_at: str | None = None
    updated_at: str | None = None
