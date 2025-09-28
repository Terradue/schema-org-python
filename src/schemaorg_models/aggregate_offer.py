from __future__ import annotations

from .offer import Offer    

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
from schemaorg_models.demand import Demand

class AggregateOffer(Offer):
    """
When a single product is associated with multiple offers (for example, the same pair of shoes is offered by different merchants), then AggregateOffer can be used.\
\
Note: AggregateOffers are normally expected to associate multiple offers that all share the same defined [[businessFunction]] value, or default to http://purl.org/goodrelations/v1#Sell if businessFunction is not explicitly defined.
    """
    class_: Literal['https://schema.org/AggregateOffer'] = Field( # type: ignore
        default='https://schema.org/AggregateOffer',
        alias='@type',
        serialization_alias='@type'
    )
    highPrice: Optional[Union[str, List[str], float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'highPrice',
            'https://schema.org/highPrice'
        ),
        serialization_alias='https://schema.org/highPrice'
    )
    lowPrice: Optional[Union[str, List[str], float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'lowPrice',
            'https://schema.org/lowPrice'
        ),
        serialization_alias='https://schema.org/lowPrice'
    )
    offerCount: Optional[Union[int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'offerCount',
            'https://schema.org/offerCount'
        ),
        serialization_alias='https://schema.org/offerCount'
    )
    offers: Optional[Union[Demand, List[Demand], Offer, List[Offer]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'offers',
            'https://schema.org/offers'
        ),
        serialization_alias='https://schema.org/offers'
    )
