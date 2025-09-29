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
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .creative_work import CreativeWork

class SocialMediaPosting(Article):
    '''
    A post to a social media platform, including blog posts, tweets, Facebook posts, etc.

    Attributes:
        sharedContent: A CreativeWork such as an image, video, or audio clip shared as part of this posting.
    '''
    class_: Literal['https://schema.org/SocialMediaPosting'] = Field( # type: ignore
        default='https://schema.org/SocialMediaPosting',
        alias='@type',
        serialization_alias='@type'
    )
    sharedContent: Optional[Union['CreativeWork', List['CreativeWork']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'sharedContent',
            'https://schema.org/sharedContent'
        ),
        serialization_alias='https://schema.org/sharedContent'
    )
