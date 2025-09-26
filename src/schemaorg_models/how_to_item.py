from typing import Union, List, Optional
from pydantic import AliasChoices, Field
from schemaorg_models.list_item import ListItem

from schemaorg_models.quantitative_value import QuantitativeValue

class HowToItem(ListItem):
    """
An item used as either a tool or supply when performing the instructions for how to achieve a result.
    """
    requiredQuantity: Optional[Union[str, List[str], float, List[float], QuantitativeValue, List[QuantitativeValue]]] = Field(default=None,validation_alias=AliasChoices('requiredQuantity', 'https://schema.org/requiredQuantity'),serialization_alias='https://schema.org/requiredQuantity')
