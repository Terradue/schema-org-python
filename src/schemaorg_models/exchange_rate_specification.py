from __future__ import annotations
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
from .structured_value import StructuredValue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .monetary_amount import MonetaryAmount
    from .unit_price_specification import UnitPriceSpecification

class ExchangeRateSpecification(StructuredValue):
    """
A structured value representing exchange rate.
    """
    class_: Literal['https://schema.org/ExchangeRateSpecification'] = Field( # type: ignore
        default='https://schema.org/ExchangeRateSpecification',
        alias='@type',
        serialization_alias='@type'
    )
    exchangeRateSpread: Optional[Union["MonetaryAmount", List["MonetaryAmount"], float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'exchangeRateSpread',
            'https://schema.org/exchangeRateSpread'
        ),
        serialization_alias='https://schema.org/exchangeRateSpread'
    )
    currency: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'currency',
            'https://schema.org/currency'
        ),
        serialization_alias='https://schema.org/currency'
    )
    currentExchangeRate: Optional[Union["UnitPriceSpecification", List["UnitPriceSpecification"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'currentExchangeRate',
            'https://schema.org/currentExchangeRate'
        ),
        serialization_alias='https://schema.org/currentExchangeRate'
    )
