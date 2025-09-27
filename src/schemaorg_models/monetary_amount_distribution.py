from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.quantitative_value_distribution import QuantitativeValueDistribution


class MonetaryAmountDistribution(QuantitativeValueDistribution):
    """
A statistical distribution of monetary amounts.
    """
    class_: Literal['https://schema.org/MonetaryAmountDistribution'] = Field(default='https://schema.org/MonetaryAmountDistribution', alias='@type', serialization_alias='@type') # type: ignore
    currency: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('currency', 'https://schema.org/currency'), serialization_alias='https://schema.org/currency')
