from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field

from .article import Article


class Metadata(BaseModel):
    abbr_name: str = Field(default_factory=str, description="Abbreviated name of the dictionary")
    short_name: str = Field(default_factory=str, description="Short name of the dictionary")
    long_name: str = Field(default_factory=str, description="Long name of the dictionary")
    verified: bool = Field(default=False, description="Verification status of the dictionary")
    ntealan: bool = Field(default=False, description="Is this a Ntealan dictionary?")
    license: str = Field(default_factory=str, description="License information")
    author_id: UUID = Field(default_factory=UUID, description="Author's unique identifier")
    source: str = Field(default_factory=str, description="Source of the dictionary")
    description: str = Field(default_factory=str, description="Description of the dictionary")
    publication: str = Field(default_factory=str, description="Publication information")
    review_year: str = Field(default_factory=str, description="Year of the last review")
    review_version: str = Field(default_factory=str, description="Version of the last review")
    src_authors: str = Field(default_factory=str, description="Source language authors")
    trg_authors: str = Field(default_factory=str, description="Target language authors")
    disable_metadata: bool = Field(default=False, description="Is the metadata disabled?")
    src_version: str = Field(default_factory=str, description="Source language version")
    trg_version: str = Field(default_factory=str, description="Target language version")


class Dictionary(Metadata):
    public_id: UUID = Field(
        default_factory=UUID,
        description="Unique public identifier for the dictionary",
        alias="dictionary_id",
    )
    articles: list[Article] | None = Field(
        default_factory=list, description="List of articles in the dictionary"
    )
    comment: str = Field(default_factory=str, description="Comments about the dictionary")
    last_update: datetime = Field(default_factory=datetime.now, description="Last update timestamp")
