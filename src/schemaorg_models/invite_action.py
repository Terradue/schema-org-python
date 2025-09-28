from __future__ import annotations
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
from .communicate_action import CommunicateAction
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .event import Event

class InviteAction(CommunicateAction):
    """
The act of asking someone to attend an event. Reciprocal of RsvpAction.
    """
    class_: Literal['https://schema.org/InviteAction'] = Field( # type: ignore
        default='https://schema.org/InviteAction',
        alias='@type',
        serialization_alias='@type'
    )
    event: Optional[Union["Event", List["Event"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'event',
            'https://schema.org/event'
        ),
        serialization_alias='https://schema.org/event'
    )
