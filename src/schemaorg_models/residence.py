from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.place import Place

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

class Residence(Place):
    """
The place where a person lives.
    """
    class_: Literal['https://schema.org/Residence'] = Field( # type: ignore
        default='https://schema.org/Residence',
        alias='@type',
        serialization_alias='@type'
    )
    accommodationFloorPlan: Optional[Union["FloorPlan", List["FloorPlan"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'accommodationFloorPlan',
            'https://schema.org/accommodationFloorPlan'
        ),
        serialization_alias='https://schema.org/accommodationFloorPlan'
    )
