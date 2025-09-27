from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.thing import Thing


class StupidType(Thing):
    """
A StupidType for testing.
    """
    class_: Literal['https://schema.org/StupidType'] = Field('class', alias='class', serialization_alias='class') # type: ignore
    stupidProperty: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = Field(default=None,validation_alias=AliasChoices('stupidProperty', 'https://schema.org/stupidProperty'), serialization_alias='https://schema.org/stupidProperty')
