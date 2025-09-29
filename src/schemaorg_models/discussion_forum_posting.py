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

class DiscussionForumPosting(SocialMediaPosting):
    '''
    A posting to a discussion forum.
    '''
    class_: Literal['https://schema.org/DiscussionForumPosting'] = Field( # type: ignore
        default='https://schema.org/DiscussionForumPosting',
        alias='@type',
        serialization_alias='@type'
    )
