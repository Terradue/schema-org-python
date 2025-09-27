from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.accommodation import Accommodation


class Apartment(Accommodation):
    """
An apartment (in American English) or flat (in British English) is a self-contained housing unit (a type of residential real estate) that occupies only part of a building (source: Wikipedia, the free encyclopedia, see <a href="http://en.wikipedia.org/wiki/Apartment">http://en.wikipedia.org/wiki/Apartment</a>).
    """
    type_: Literal['https://schema.org/Apartment'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Apartment'),serialization_alias='class') # type: ignore
    occupancy: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = Field(default=None,validation_alias=AliasChoices('occupancy', 'https://schema.org/occupancy'),serialization_alias='https://schema.org/occupancy')
    numberOfRooms: Optional[Union[float, List[float], "QuantitativeValue", List["QuantitativeValue"]]] = Field(default=None,validation_alias=AliasChoices('numberOfRooms', 'https://schema.org/numberOfRooms'),serialization_alias='https://schema.org/numberOfRooms')
