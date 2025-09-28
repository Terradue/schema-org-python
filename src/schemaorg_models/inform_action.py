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

class InformAction(CommunicateAction):
    """
The act of notifying someone of information pertinent to them, with no expectation of a response.
    """
    class_: Literal['https://schema.org/InformAction'] = Field( # type: ignore
        default='https://schema.org/InformAction',
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
