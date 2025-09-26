from typing import Union, List, Optional
from pydantic import AliasChoices, Field
from schemaorg_models.place import Place


class Residence(Place):
    """
The place where a person lives.
    """
    accommodationFloorPlan: Optional[Union["FloorPlan", List["FloorPlan"]]] = Field(default=None,validation_alias=AliasChoices('accommodationFloorPlan', 'https://schema.org/accommodationFloorPlan'),serialization_alias='https://schema.org/accommodationFloorPlan')
