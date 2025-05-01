from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field

from .contribution import Contribution


class Article(BaseModel):
    public_id: UUID = Field(
        default_factory=UUID,
        description="Unique public identifier for the article",
        alias="article_id",
    )
    id_dico: UUID = Field(
        default_factory=UUID,
        description="Dictionary ID to which the article belongs",
        alias="dictionary_id",
    )
    typ_article: str = Field(default_factory=str, description="Type of the article")
    classe: str = Field(default_factory=str, description="Class/category of the article")
    verified: bool = Field(
        default_factory=bool,
        description="Verification status of the article",
    )
    license: str = Field(default_factory=str, description="License information for the article")
    ntealan: bool = Field(default_factory=bool, description="Is the article from Ntealan?")
    form: str = Field(default_factory=str, description="Form of the article")
    entry: str = Field(default_factory=str, description="Entry word or phrase")
    category: str = Field(default_factory=str, description="Category of the article")
    example: str = Field(default_factory=str, description="Example usage of the entry")
    translate_fr: str = Field(default_factory=str, description="French translation")
    translate_en: str = Field(default_factory=str, description="English translation")
    translate_es: str = Field(default_factory=str, description="Spanish translation")
    translate_ko: str = Field(default_factory=str, description="Korean translation")
    author_id: str = Field(default_factory=str, description="Author's identifier")
    all_content: str = Field(default_factory=str, description="All content of the article")
    media: str = Field(default_factory=str, description="Media associated with the article")
    radical: str = Field(default_factory=str, description="Radical/root of the entry")
    translate_african: str = Field(default_factory=str, description="African language translation")
    users_versions: str = Field(default_factory=str, description="User versions of the article")
    all_raw_text: str = Field(default_factory=str, description="All raw text of the article")
    disable_article: bool = Field(default_factory=bool, description="Is the article disabled?")
    html_version: str = Field(default_factory=str, description="HTML version of the article")
    like: int = Field(default_factory=int, description="Number of likes")
    unlike: int = Field(default_factory=int, description="Number of unlikes")
    viewers: int = Field(default_factory=int, description="Number of viewers")
    contributions: list[Contribution] | None = Field(
        description="List of contributions to the article"
    )
    last_update: datetime = Field(default_factory=datetime.now, description="Last update timestamp")
