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
from .action import Action
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .price_specification import PriceSpecification

class TradeAction(Action):
    '''
    The act of participating in an exchange of goods and services for monetary compensation. An agent trades an object, product or service with a participant in exchange for a one time or periodic payment.

    Attributes:
        price: The offer price of a product, or of a price component when attached to PriceSpecification and its subtypes.\
\
Usage guidelines:\
\
* Use the [[priceCurrency]] property (with standard formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217), e.g. "USD"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) for cryptocurrencies, e.g. "BTC"; well known names for [Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system) (LETS) and other currency types, e.g. "Ithaca HOUR") instead of including [ambiguous symbols](http://en.wikipedia.org/wiki/Dollar_sign#Currencies_that_use_the_dollar_or_peso_sign) such as '$' in the value.\
* Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator.\
* Note that both [RDFa](http://www.w3.org/TR/xhtml-rdfa-primer/#using-the-content-attribute) and Microdata syntax allow the use of a "content=" attribute for publishing simple machine-readable values alongside more human-friendly formatting.\
* Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similar Unicode symbols.
      
        priceCurrency: The currency of the price, or a price component when attached to [[PriceSpecification]] and its subtypes.\
\
Use standard formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217), e.g. "USD"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) for cryptocurrencies, e.g. "BTC"; well known names for [Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system) (LETS) and other currency types, e.g. "Ithaca HOUR".
        priceSpecification: One or more detailed price specifications, indicating the unit price and delivery or payment charges.
    '''
    class_: Literal['https://schema.org/TradeAction'] = Field( # type: ignore
        default='https://schema.org/TradeAction',
        alias='@type',
        serialization_alias='@type'
    )
    price: Optional[Union[str, List[str], float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    priceCurrency: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    priceSpecification: Optional[Union['PriceSpecification', List['PriceSpecification']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
