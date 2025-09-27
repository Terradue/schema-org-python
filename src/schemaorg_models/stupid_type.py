from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.thing import Thing


class StupidType(Thing):
    """
A StupidType for testing.
    """
    class_: Literal['https://schema.org/StupidType'] = Field(default='https://schema.org/StupidType', alias='@type', serialization_alias='@type') # type: ignore
    stupidProperty: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = Field(default=None, validation_alias=AliasChoices('stupidProperty', 'https://schema.org/stupidProperty'), serialization_alias='https://schema.org/stupidProperty')
