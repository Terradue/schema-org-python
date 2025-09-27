from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.list_item import ListItem

from schemaorg_models.quantitative_value import QuantitativeValue

class HowToItem(ListItem):
    """
An item used as either a tool or supply when performing the instructions for how to achieve a result.
    """
    class_: Literal['https://schema.org/HowToItem'] = Field(default='https://schema.org/HowToItem', alias='class', serialization_alias='class') # type: ignore
    requiredQuantity: Optional[Union[str, List[str], float, List[float], QuantitativeValue, List[QuantitativeValue]]] = Field(default=None, validation_alias=AliasChoices('requiredQuantity', 'https://schema.org/requiredQuantity'), serialization_alias='https://schema.org/requiredQuantity')
