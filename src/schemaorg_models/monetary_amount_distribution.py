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
from .quantitative_value_distribution import QuantitativeValueDistribution

class MonetaryAmountDistribution(QuantitativeValueDistribution):
    '''
    A statistical distribution of monetary amounts.

    Attributes:
        currency: The currency in which the monetary amount is expressed.\
\
Use standard formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217), e.g. "USD"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) for cryptocurrencies, e.g. "BTC"; well known names for [Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system) (LETS) and other currency types, e.g. "Ithaca HOUR".
    '''
    class_: Literal['https://schema.org/MonetaryAmountDistribution'] = Field( # type: ignore
        default='https://schema.org/MonetaryAmountDistribution',
        alias='@type',
        serialization_alias='@type'
    )
    currency: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
