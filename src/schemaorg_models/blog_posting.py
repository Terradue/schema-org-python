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
from .social_media_posting import SocialMediaPosting

class BlogPosting(SocialMediaPosting):
    '''
    A blog post.
    '''
    class_: Literal['https://schema.org/BlogPosting'] = Field( # type: ignore
        default='https://schema.org/BlogPosting',
        alias='@type',
        serialization_alias='@type'
    )
