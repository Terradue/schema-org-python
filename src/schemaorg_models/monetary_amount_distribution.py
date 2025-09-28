from __future__ import annotations

from .quantitative_value_distribution import QuantitativeValueDistribution    

from pydantic import (
    AliasChoices,
    Field
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)

class MonetaryAmountDistribution(QuantitativeValueDistribution):
    """
A statistical distribution of monetary amounts.
    """
    class_: Literal['https://schema.org/MonetaryAmountDistribution'] = Field( # type: ignore
        default='https://schema.org/MonetaryAmountDistribution',
        alias='@type',
        serialization_alias='@type'
    )
    currency: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'currency',
            'https://schema.org/currency'
        ),
        serialization_alias='https://schema.org/currency'
    )
