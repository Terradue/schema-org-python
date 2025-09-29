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
from .place import Place
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .organization import Organization

class LocalBusiness(Place):
    '''
    A particular physical business or branch of an organization. Examples of LocalBusiness include a restaurant, a particular branch of a restaurant chain, a branch of a bank, a medical practice, a club, a bowling alley, etc.

    Attributes:
        paymentAccepted: Cash, Credit Card, Cryptocurrency, Local Exchange Tradings System, etc.
        priceRange: The price range of the business, for example ```$$$```.
        branchOf: The larger organization that this local business is a branch of, if any. Not to be confused with (anatomical) [[branch]].
        currenciesAccepted: The currency accepted.\
\
Use standard formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217), e.g. "USD"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) for cryptocurrencies, e.g. "BTC"; well known names for [Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system) (LETS) and other currency types, e.g. "Ithaca HOUR".
        openingHours: The general opening hours for a business. Opening hours can be specified as a weekly time range, starting with days, then times per day. Multiple days can be listed with commas ',' separating each day. Day or time ranges are specified using a hyphen '-'.\
\
* Days are specified using the following two-letter combinations: ```Mo```, ```Tu```, ```We```, ```Th```, ```Fr```, ```Sa```, ```Su```.\
* Times are specified using 24:00 format. For example, 3pm is specified as ```15:00```, 10am as ```10:00```. \
* Here is an example: <code>&lt;time itemprop="openingHours" datetime=&quot;Tu,Th 16:00-20:00&quot;&gt;Tuesdays and Thursdays 4-8pm&lt;/time&gt;</code>.\
* If a business is open 7 days a week, then it can be specified as <code>&lt;time itemprop=&quot;openingHours&quot; datetime=&quot;Mo-Su&quot;&gt;Monday through Sunday, all day&lt;/time&gt;</code>.
    '''
    class_: Literal['https://schema.org/LocalBusiness'] = Field( # type: ignore
        default='https://schema.org/LocalBusiness',
        alias='@type',
        serialization_alias='@type'
    )
    paymentAccepted: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    priceRange: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    branchOf: Optional[Union['Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    currenciesAccepted: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    openingHours: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
