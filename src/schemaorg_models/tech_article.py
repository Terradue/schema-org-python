from __future__ import annotations
from datetime import (
    date,
    datetime,
    time
)
from pydantic import (
    field_serializer,
    field_validator,
    AliasChoices,
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .article import Article

class TechArticle(Article):
    '''
    A technical article - Example: How-to (task) topics, step-by-step, procedural troubleshooting, specifications, etc.

    Attributes:
        proficiencyLevel: Proficiency needed for this content; expected values: 'Beginner', 'Expert'.
        dependencies: Prerequisites needed to fulfill steps in article.
    '''
    class_: Literal['https://schema.org/TechArticle'] = Field( # type: ignore
        default='https://schema.org/TechArticle',
        alias='@type',
        serialization_alias='@type'
    )
    proficiencyLevel: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    dependencies: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
