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
from .place import Place
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .floor_plan import FloorPlan

class Residence(Place):
    '''
    The place where a person lives.

    Attributes:
        accommodationFloorPlan: A floorplan of some [[Accommodation]].
    '''
    class_: Literal['https://schema.org/Residence'] = Field( # type: ignore
        default='https://schema.org/Residence',
        alias='@type',
        serialization_alias='@type'
    )
    accommodationFloorPlan: Optional[Union['FloorPlan', List['FloorPlan']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'accommodationFloorPlan',
            'https://schema.org/accommodationFloorPlan'
        ),
        serialization_alias='https://schema.org/accommodationFloorPlan'
    )
