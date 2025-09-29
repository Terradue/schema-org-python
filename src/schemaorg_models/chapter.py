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
from .creative_work import CreativeWork

class Chapter(CreativeWork):
    '''
    One of the sections into which a book is divided. A chapter usually has a section number or a name.

    Attributes:
        pageStart: The page on which the work starts; for example "135" or "xiii".
        pagination: Any description of pages that is not separated into pageStart and pageEnd; for example, "1-6, 9, 55" or "10-12, 46-49".
        pageEnd: The page on which the work ends; for example "138" or "xvi".
    '''
    class_: Literal['https://schema.org/Chapter'] = Field( # type: ignore
        default='https://schema.org/Chapter',
        alias='@type',
        serialization_alias='@type'
    )
    pageStart: Optional[Union[int, List[int], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    pagination: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    pageEnd: Optional[Union[str, List[str], int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
