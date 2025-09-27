from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.civic_structure import CivicStructure


class Airport(CivicStructure):
    """
An airport.
    """
    class_: Literal['https://schema.org/Airport'] = Field('class', alias='class', serialization_alias='class') # type: ignore
    iataCode: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('iataCode', 'https://schema.org/iataCode'), serialization_alias='https://schema.org/iataCode')
    icaoCode: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('icaoCode', 'https://schema.org/icaoCode'), serialization_alias='https://schema.org/icaoCode')
