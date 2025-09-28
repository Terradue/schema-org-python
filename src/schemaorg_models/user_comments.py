from __future__ import annotations
from datetime import (
    date,
    datetime
)
from pydantic import (
    AliasChoices,
    Field,
    HttpUrl
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .user_interaction import UserInteraction
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .organization import Organization
    from .person import Person
    from .creative_work import CreativeWork

class UserComments(UserInteraction):
    """
UserInteraction and its subtypes is an old way of talking about users interacting with pages. It is generally better to use [[Action]]-based vocabulary, alongside types such as [[Comment]].
    """
    class_: Literal['https://schema.org/UserComments'] = Field( # type: ignore
        default='https://schema.org/UserComments',
        alias='@type',
        serialization_alias='@type'
    )
    commentTime: Optional[Union[date, List[date], datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'commentTime',
            'https://schema.org/commentTime'
        ),
        serialization_alias='https://schema.org/commentTime'
    )
    replyToUrl: Optional[Union[HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'replyToUrl',
            'https://schema.org/replyToUrl'
        ),
        serialization_alias='https://schema.org/replyToUrl'
    )
    creator: Optional[Union["Person", List["Person"], "Organization", List["Organization"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'creator',
            'https://schema.org/creator'
        ),
        serialization_alias='https://schema.org/creator'
    )
    discusses: Optional[Union["CreativeWork", List["CreativeWork"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'discusses',
            'https://schema.org/discusses'
        ),
        serialization_alias='https://schema.org/discusses'
    )
    commentText: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'commentText',
            'https://schema.org/commentText'
        ),
        serialization_alias='https://schema.org/commentText'
    )
