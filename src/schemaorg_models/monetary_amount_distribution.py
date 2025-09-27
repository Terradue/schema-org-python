from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.quantitative_value_distribution import QuantitativeValueDistribution


class MonetaryAmountDistribution(QuantitativeValueDistribution):
    """
A statistical distribution of monetary amounts.
    """
    type_: Literal['https://schema.org/MonetaryAmountDistribution'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/MonetaryAmountDistribution'),serialization_alias='class') # type: ignore
    currency: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('currency', 'https://schema.org/currency'),serialization_alias='https://schema.org/currency')
