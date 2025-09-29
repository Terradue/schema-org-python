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
from .inform_action import InformAction
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .comment import Comment
    from .rsvp_response_type import RsvpResponseType

class RsvpAction(InformAction):
    '''
    The act of notifying an event organizer as to whether you expect to attend the event.

    Attributes:
        additionalNumberOfGuests: If responding yes, the number of guests who will attend in addition to the invitee.
        comment: Comments, typically from users.
        rsvpResponse: The response (yes, no, maybe) to the RSVP.
    '''
    class_: Literal['https://schema.org/RsvpAction'] = Field( # type: ignore
        default='https://schema.org/RsvpAction',
        alias='@type',
        serialization_alias='@type'
    )
    additionalNumberOfGuests: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    comment: Optional[Union['Comment', List['Comment']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    rsvpResponse: Optional[Union['RsvpResponseType', List['RsvpResponseType']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
