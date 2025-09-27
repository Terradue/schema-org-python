from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.thing import Thing


class StupidType(Thing):
    """
A StupidType for testing.
    """
    type_: Literal['https://schema.org/StupidType'] = Field(default='https://schema.org/StupidType', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
    stupidProperty: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = Field(default=None, validation_alias=AliasChoices('stupidProperty', 'https://schema.org/stupidProperty'), serialization_alias='https://schema.org/stupidProperty')
