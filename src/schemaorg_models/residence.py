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
from .floor_plan import FloorPlan
from .place import Place

class Residence(Place):
    """
The place where a person lives.
    """
    class_: Literal['https://schema.org/Residence'] = Field( # type: ignore
        default='https://schema.org/Residence',
        alias='@type',
        serialization_alias='@type'
    )
    accommodationFloorPlan: Optional[Union[FloorPlan, List[FloorPlan]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'accommodationFloorPlan',
            'https://schema.org/accommodationFloorPlan'
        ),
        serialization_alias='https://schema.org/accommodationFloorPlan'
    )
