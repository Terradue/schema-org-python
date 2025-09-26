from typing import Union, List, Optional
from pydantic import AliasChoices, Field
from schemaorg_models.thing import Thing


class StupidType(Thing):
    """
A StupidType for testing.
    """
    stupidProperty: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = Field(default=None,validation_alias=AliasChoices('stupidProperty', 'https://schema.org/stupidProperty'),serialization_alias='https://schema.org/stupidProperty')
