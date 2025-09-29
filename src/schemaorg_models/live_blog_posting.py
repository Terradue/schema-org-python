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
from .blog_posting import BlogPosting

class LiveBlogPosting(BlogPosting):
    '''
    A [[LiveBlogPosting]] is a [[BlogPosting]] intended to provide a rolling textual coverage of an ongoing event through continuous updates.

    Attributes:
        liveBlogUpdate: An update to the LiveBlog.
        coverageStartTime: The time when the live blog will begin covering the Event. Note that coverage may begin before the Event's start time. The LiveBlogPosting may also be created before coverage begins.
        coverageEndTime: The time when the live blog will stop covering the Event. Note that coverage may continue after the Event concludes.
    '''
    class_: Literal['https://schema.org/LiveBlogPosting'] = Field( # type: ignore
        default='https://schema.org/LiveBlogPosting',
        alias='@type',
        serialization_alias='@type'
    )
    liveBlogUpdate: Optional[Union['BlogPosting', List['BlogPosting']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    coverageStartTime: Optional[Union[datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    coverageEndTime: Optional[Union[datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
