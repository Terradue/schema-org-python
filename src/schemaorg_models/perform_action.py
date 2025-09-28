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
from .play_action import PlayAction
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .entertainment_business import EntertainmentBusiness

class PerformAction(PlayAction):
    """
The act of participating in performance arts.
    """
    class_: Literal['https://schema.org/PerformAction'] = Field( # type: ignore
        default='https://schema.org/PerformAction',
        alias='@type',
        serialization_alias='@type'
    )
    entertainmentBusiness: Optional[Union["EntertainmentBusiness", List["EntertainmentBusiness"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'entertainmentBusiness',
            'https://schema.org/entertainmentBusiness'
        ),
        serialization_alias='https://schema.org/entertainmentBusiness'
    )
