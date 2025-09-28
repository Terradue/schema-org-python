from __future__ import annotations
from datetime import (
    datetime
)
from pydantic import (
    AliasChoices,
    Field
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .blog_posting import BlogPosting

class LiveBlogPosting(BlogPosting):
    """
A [[LiveBlogPosting]] is a [[BlogPosting]] intended to provide a rolling textual coverage of an ongoing event through continuous updates.
    """
    class_: Literal['https://schema.org/LiveBlogPosting'] = Field( # type: ignore
        default='https://schema.org/LiveBlogPosting',
        alias='@type',
        serialization_alias='@type'
    )
    liveBlogUpdate: Optional[Union["BlogPosting", List["BlogPosting"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'liveBlogUpdate',
            'https://schema.org/liveBlogUpdate'
        ),
        serialization_alias='https://schema.org/liveBlogUpdate'
    )
    coverageStartTime: Optional[Union[datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'coverageStartTime',
            'https://schema.org/coverageStartTime'
        ),
        serialization_alias='https://schema.org/coverageStartTime'
    )
    coverageEndTime: Optional[Union[datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'coverageEndTime',
            'https://schema.org/coverageEndTime'
        ),
        serialization_alias='https://schema.org/coverageEndTime'
    )
