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
from .move_action import MoveAction
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .distance import Distance

class TravelAction(MoveAction):
    '''
    The act of traveling from a fromLocation to a destination by a specified mode of transport, optionally with participants.

    Attributes:
        distance: The distance travelled, e.g. exercising or travelling.
    '''
    class_: Literal['https://schema.org/TravelAction'] = Field( # type: ignore
        default='https://schema.org/TravelAction',
        alias='@type',
        serialization_alias='@type'
    )
    distance: Optional[Union['Distance', List['Distance']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'distance',
            'https://schema.org/distance'
        ),
        serialization_alias='https://schema.org/distance'
    )
