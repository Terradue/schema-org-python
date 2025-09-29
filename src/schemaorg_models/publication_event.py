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
from .event import Event
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .broadcast_service import BroadcastService
    from .organization import Organization
    from .person import Person

class PublicationEvent(Event):
    '''
    A PublicationEvent corresponds indifferently to the event of publication for a CreativeWork of any type, e.g. a broadcast event, an on-demand event, a book/journal publication via a variety of delivery media.

    Attributes:
        publishedBy: An agent associated with the publication event.
        publishedOn: A broadcast service associated with the publication event.
        free: A flag to signal that the item, event, or place is accessible for free.
    '''
    class_: Literal['https://schema.org/PublicationEvent'] = Field( # type: ignore
        default='https://schema.org/PublicationEvent',
        alias='@type',
        serialization_alias='@type'
    )
    publishedBy: Optional[Union['Organization', List['Organization'], 'Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'publishedBy',
            'https://schema.org/publishedBy'
        ),
        serialization_alias='https://schema.org/publishedBy'
    )
    publishedOn: Optional[Union['BroadcastService', List['BroadcastService']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'publishedOn',
            'https://schema.org/publishedOn'
        ),
        serialization_alias='https://schema.org/publishedOn'
    )
    free: Optional[Union[bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'free',
            'https://schema.org/free'
        ),
        serialization_alias='https://schema.org/free'
    )
