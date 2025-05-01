from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field


class Contribution(BaseModel):
    public_id: UUID = Field(
        default_factory=UUID, description="Unique public identifier for the contribution"
    )
    dico_id: UUID = Field(
        default_factory=UUID,
        description="Dictionary ID associated with the contribution",
        alias="dictionary_id",
    )
    user_id: UUID = Field(default_factory=UUID, description="User ID of the contributor")
    article_id: UUID = Field(
        default_factory=UUID, description="Article ID associated with the contribution"
    )
    user_name: str = Field(default_factory=str, description="Name of the user who contributed")
    contrib_type: str = Field(default_factory=str, description="Type of contribution")
    contrib_path: str = Field(
        default_factory=str, description="Path or location of the contribution"
    )
    contrib_data: str = Field(default_factory=str, description="Data/content of the contribution")
    contrib_name: str = Field(default_factory=str, description="Name/title of the contribution")
    ntealan: bool = Field(default_factory=bool, description="Is the contribution from Ntealan?")
    validated: bool = Field(
        default_factory=bool, description="Validation status of the contribution", alias="validate"
    )
    last_update: datetime = Field(default_factory=datetime.now, description="Last update timestamp")
