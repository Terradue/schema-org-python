from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.place import Place


class Residence(Place):
    """
The place where a person lives.
    """
    class_: Literal['https://schema.org/Residence'] = Field(default='https://schema.org/Residence', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
    accommodationFloorPlan: Optional[Union["FloorPlan", List["FloorPlan"]]] = Field(default=None, validation_alias=AliasChoices('accommodationFloorPlan', 'https://schema.org/accommodationFloorPlan'), serialization_alias='https://schema.org/accommodationFloorPlan')
