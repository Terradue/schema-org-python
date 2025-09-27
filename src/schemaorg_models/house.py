from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.accommodation import Accommodation


class House(Accommodation):
    """
A house is a building or structure that has the ability to be occupied for habitation by humans or other creatures (source: Wikipedia, the free encyclopedia, see <a href="http://en.wikipedia.org/wiki/House">http://en.wikipedia.org/wiki/House</a>).
    """
    class_: Literal['https://schema.org/House'] = Field(default='https://schema.org/House', alias='class', serialization_alias='class') # type: ignore
    numberOfRooms: Optional[Union[float, List[float], "QuantitativeValue", List["QuantitativeValue"]]] = Field(default=None, validation_alias=AliasChoices('numberOfRooms', 'https://schema.org/numberOfRooms'), serialization_alias='https://schema.org/numberOfRooms')
