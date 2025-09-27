from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.house import House

from schemaorg_models.quantitative_value import QuantitativeValue

class SingleFamilyResidence(House):
    """
Residence type: Single-family home.
    """
    class_: Literal['https://schema.org/SingleFamilyResidence'] = Field('class', alias='class', serialization_alias='class') # type: ignore
    numberOfRooms: Optional[Union[float, List[float], QuantitativeValue, List[QuantitativeValue]]] = Field(default=None,validation_alias=AliasChoices('numberOfRooms', 'https://schema.org/numberOfRooms'), serialization_alias='https://schema.org/numberOfRooms')
    occupancy: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = Field(default=None,validation_alias=AliasChoices('occupancy', 'https://schema.org/occupancy'), serialization_alias='https://schema.org/occupancy')
