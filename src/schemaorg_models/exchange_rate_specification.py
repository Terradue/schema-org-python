from __future__ import annotations
from datetime import (
    date,
    datetime,
    time
)
from pydantic import (
    field_serializer,
    field_validator,
    AliasChoices,
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl
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
    from .unit_price_specification import UnitPriceSpecification
    from .monetary_amount import MonetaryAmount

class ExchangeRateSpecification(StructuredValue):
    '''
    A structured value representing exchange rate.

    Attributes:
        exchangeRateSpread: The difference between the price at which a broker or other intermediary buys and sells foreign currency.
        currency: The currency in which the monetary amount is expressed.\
\
Use standard formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217), e.g. "USD"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) for cryptocurrencies, e.g. "BTC"; well known names for [Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system) (LETS) and other currency types, e.g. "Ithaca HOUR".
        currentExchangeRate: The current price of a currency.
    '''
    class_: Literal['https://schema.org/ExchangeRateSpecification'] = Field( # type: ignore
        default='https://schema.org/ExchangeRateSpecification',
        alias='@type',
        serialization_alias='@type'
    )
    exchangeRateSpread: Optional[Union['MonetaryAmount', List['MonetaryAmount'], float, List[float]]] = Field(
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
    currentExchangeRate: Optional[Union['UnitPriceSpecification', List['UnitPriceSpecification']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'currentExchangeRate',
            'https://schema.org/currentExchangeRate'
        ),
        serialization_alias='https://schema.org/currentExchangeRate'
    )
