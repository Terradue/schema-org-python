from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.place import Place


class Residence(Place):
    """
The place where a person lives.
    """
    type_: Literal['https://schema.org/Residence'] = Field(default='https://schema.org/Residence', alias='@type', serialization_alias='@type') # type: ignore
    accommodationFloorPlan: Optional[Union["FloorPlan", List["FloorPlan"]]] = Field(default=None, validation_alias=AliasChoices('accommodationFloorPlan', 'https://schema.org/accommodationFloorPlan'), serialization_alias='https://schema.org/accommodationFloorPlan')
