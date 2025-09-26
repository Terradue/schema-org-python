from typing import Union, List, Optional
from pydantic import AliasChoices, Field
from schemaorg_models.how_to_item import HowToItem

from schemaorg_models.monetary_amount import MonetaryAmount

class HowToSupply(HowToItem):
    """
A supply consumed when performing the instructions for how to achieve a result.
    """
    estimatedCost: Optional[Union[str, List[str], MonetaryAmount, List[MonetaryAmount]]] = Field(default=None,validation_alias=AliasChoices('estimatedCost', 'https://schema.org/estimatedCost'),serialization_alias='https://schema.org/estimatedCost')
