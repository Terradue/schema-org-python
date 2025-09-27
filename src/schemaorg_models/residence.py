from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.place import Place


class Residence(Place):
    """
The place where a person lives.
    """
    type_: Literal['https://schema.org/Residence'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Residence'),serialization_alias='class') # type: ignore
    accommodationFloorPlan: Optional[Union["FloorPlan", List["FloorPlan"]]] = Field(default=None,validation_alias=AliasChoices('accommodationFloorPlan', 'https://schema.org/accommodationFloorPlan'),serialization_alias='https://schema.org/accommodationFloorPlan')
