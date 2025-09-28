from __future__ import annotations

from .move_action import MoveAction    

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
from schemaorg_models.distance import Distance

class TravelAction(MoveAction):
    """
The act of traveling from a fromLocation to a destination by a specified mode of transport, optionally with participants.
    """
    class_: Literal['https://schema.org/TravelAction'] = Field( # type: ignore
        default='https://schema.org/TravelAction',
        alias='@type',
        serialization_alias='@type'
    )
    distance: Optional[Union[Distance, List[Distance]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'distance',
            'https://schema.org/distance'
        ),
        serialization_alias='https://schema.org/distance'
    )
