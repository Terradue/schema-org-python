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
from .intangible import Intangible
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .demand import Demand
    from .item_list import ItemList
    from .person import Person
    from .place import Place
    from .organization import Organization
    from .offer import Offer

class Trip(Intangible):
    '''
    A trip or journey. An itinerary of visits to one or more places.

    Attributes:
        subTrip: Identifies a [[Trip]] that is a subTrip of this Trip.  For example Day 1, Day 2, etc. of a multi-day trip.
        provider: The service provider, service operator, or service performer; the goods producer. Another party (a seller) may offer those services or goods on behalf of the provider. A provider may also serve as the seller.
        partOfTrip: Identifies that this [[Trip]] is a subTrip of another Trip.  For example Day 1, Day 2, etc. of a multi-day trip.
        departureTime: The expected departure time.
        tripOrigin: The location of origin of the trip, prior to any destination(s).
        itinerary: Destination(s) ( [[Place]] ) that make up a trip. For a trip where destination order is important use [[ItemList]] to specify that order (see examples).
        arrivalTime: The expected arrival time.
        offers: An offer to provide this item&#x2014;for example, an offer to sell a product, rent the DVD of a movie, perform a service, or give away tickets to an event. Use [[businessFunction]] to indicate the kind of transaction offered, i.e. sell, lease, etc. This property can also be used to describe a [[Demand]]. While this property is listed as expected on a number of common types, it can be used in others. In that case, using a second type, such as Product or a subtype of Product, can clarify the nature of the offer.
      
    '''
    class_: Literal['https://schema.org/Trip'] = Field( # type: ignore
        default='https://schema.org/Trip',
        alias='@type',
        serialization_alias='@type'
    )
    subTrip: Optional[Union['Trip', List['Trip']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    provider: Optional[Union['Person', List['Person'], 'Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    partOfTrip: Optional[Union['Trip', List['Trip']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    departureTime: Optional[Union[time, List[time], datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    tripOrigin: Optional[Union['Place', List['Place']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    itinerary: Optional[Union['ItemList', List['ItemList'], 'Place', List['Place']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    arrivalTime: Optional[Union[time, List[time], datetime, List[datetime]]] = Field(
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
