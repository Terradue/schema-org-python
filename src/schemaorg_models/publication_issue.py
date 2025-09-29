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

class PublicationIssue(CreativeWork):
    '''
    A part of a successively published publication such as a periodical or publication volume, often numbered, usually containing a grouping of works such as articles.\
\
See also [blog post](https://blog-schema.org/2014/09/02/schema-org-support-for-bibliographic-relationships-and-periodicals/).

    Attributes:
        pagination: Any description of pages that is not separated into pageStart and pageEnd; for example, "1-6, 9, 55" or "10-12, 46-49".
        pageStart: The page on which the work starts; for example "135" or "xiii".
        issueNumber: Identifies the issue of publication; for example, "iii" or "2".
        pageEnd: The page on which the work ends; for example "138" or "xvi".
    '''
    class_: Literal['https://schema.org/PublicationIssue'] = Field( # type: ignore
        default='https://schema.org/PublicationIssue',
        alias='@type',
        serialization_alias='@type'
    )
    pagination: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    pageStart: Optional[Union[int, List[int], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    issueNumber: Optional[Union[str, List[str], int, List[int]]] = Field(
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
