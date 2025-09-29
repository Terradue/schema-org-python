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
from .offer import Offer
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .demand import Demand

class AggregateOffer(Offer):
    '''
    When a single product is associated with multiple offers (for example, the same pair of shoes is offered by different merchants), then AggregateOffer can be used.\
\
Note: AggregateOffers are normally expected to associate multiple offers that all share the same defined [[businessFunction]] value, or default to http://purl.org/goodrelations/v1#Sell if businessFunction is not explicitly defined.

    Attributes:
        highPrice: The highest price of all offers available.\
\
Usage guidelines:\
\
* Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similar Unicode symbols.\
* Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator.
        lowPrice: The lowest price of all offers available.\
\
Usage guidelines:\
\
* Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similar Unicode symbols.\
* Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator.
        offerCount: The number of offers for the product.
        offers: An offer to provide this item&#x2014;for example, an offer to sell a product, rent the DVD of a movie, perform a service, or give away tickets to an event. Use [[businessFunction]] to indicate the kind of transaction offered, i.e. sell, lease, etc. This property can also be used to describe a [[Demand]]. While this property is listed as expected on a number of common types, it can be used in others. In that case, using a second type, such as Product or a subtype of Product, can clarify the nature of the offer.
      
    '''
    class_: Literal['https://schema.org/AggregateOffer'] = Field( # type: ignore
        default='https://schema.org/AggregateOffer',
        alias='@type',
        serialization_alias='@type'
    )
    highPrice: Optional[Union[str, List[str], float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    lowPrice: Optional[Union[str, List[str], float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    offerCount: Optional[Union[int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    offers: Optional[Union['Demand', List['Demand'], 'Offer', List['Offer']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
