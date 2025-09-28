from __future__ import annotations
from datetime import (
    datetime,
    time
)
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
from .intangible import Intangible
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .demand import Demand
    from .organization import Organization
    from .offer import Offer
    from .person import Person
    from .place import Place
    from .item_list import ItemList

class Trip(Intangible):
    """
A trip or journey. An itinerary of visits to one or more places.
    """
    class_: Literal['https://schema.org/Trip'] = Field( # type: ignore
        default='https://schema.org/Trip',
        alias='@type',
        serialization_alias='@type'
    )
    subTrip: Optional[Union["Trip", List["Trip"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'subTrip',
            'https://schema.org/subTrip'
        ),
        serialization_alias='https://schema.org/subTrip'
    )
    provider: Optional[Union["Person", List["Person"], "Organization", List["Organization"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'provider',
            'https://schema.org/provider'
        ),
        serialization_alias='https://schema.org/provider'
    )
    partOfTrip: Optional[Union["Trip", List["Trip"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'partOfTrip',
            'https://schema.org/partOfTrip'
        ),
        serialization_alias='https://schema.org/partOfTrip'
    )
    departureTime: Optional[Union[time, List[time], datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'departureTime',
            'https://schema.org/departureTime'
        ),
        serialization_alias='https://schema.org/departureTime'
    )
    tripOrigin: Optional[Union["Place", List["Place"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'tripOrigin',
            'https://schema.org/tripOrigin'
        ),
        serialization_alias='https://schema.org/tripOrigin'
    )
    itinerary: Optional[Union["ItemList", List["ItemList"], "Place", List["Place"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'itinerary',
            'https://schema.org/itinerary'
        ),
        serialization_alias='https://schema.org/itinerary'
    )
    arrivalTime: Optional[Union[time, List[time], datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'arrivalTime',
            'https://schema.org/arrivalTime'
        ),
        serialization_alias='https://schema.org/arrivalTime'
    )
    offers: Optional[Union["Demand", List["Demand"], "Offer", List["Offer"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'offers',
            'https://schema.org/offers'
        ),
        serialization_alias='https://schema.org/offers'
    )
