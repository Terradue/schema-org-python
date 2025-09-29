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
from .user_interaction import UserInteraction
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .creative_work import CreativeWork
    from .organization import Organization
    from .person import Person

class UserComments(UserInteraction):
    '''
    UserInteraction and its subtypes is an old way of talking about users interacting with pages. It is generally better to use [[Action]]-based vocabulary, alongside types such as [[Comment]].

    Attributes:
        commentTime: The time at which the UserComment was made.
        replyToUrl: The URL at which a reply may be posted to the specified UserComment.
        creator: The creator/author of this CreativeWork. This is the same as the Author property for CreativeWork.
        discusses: Specifies the CreativeWork associated with the UserComment.
        commentText: The text of the UserComment.
    '''
    class_: Literal['https://schema.org/UserComments'] = Field( # type: ignore
        default='https://schema.org/UserComments',
        alias='@type',
        serialization_alias='@type'
    )
    commentTime: Optional[Union[date, List[date], datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    replyToUrl: Optional[Union[HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    creator: Optional[Union['Person', List['Person'], 'Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    discusses: Optional[Union['CreativeWork', List['CreativeWork']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    commentText: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
