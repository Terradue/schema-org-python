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
from .communicate_action import CommunicateAction
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .event import Event

class InviteAction(CommunicateAction):
    '''
    The act of asking someone to attend an event. Reciprocal of RsvpAction.

    Attributes:
        event: Upcoming or past event associated with this place, organization, or action.
    '''
    class_: Literal['https://schema.org/InviteAction'] = Field( # type: ignore
        default='https://schema.org/InviteAction',
        alias='@type',
        serialization_alias='@type'
    )
    event: Optional[Union['Event', List['Event']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
