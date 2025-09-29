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
from .trip import Trip
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .vehicle import Vehicle
    from .person import Person
    from .distance import Distance
    from .boarding_policy_type import BoardingPolicyType
    from .organization import Organization
    from .duration import Duration
    from .airport import Airport

class Flight(Trip):
    '''
    An airline flight.

    Attributes:
        boardingPolicy: The type of boarding policy used by the airline (e.g. zone-based or group-based).
        estimatedFlightDuration: The estimated time the flight will take.
        departureAirport: The airport where the flight originates.
        carrier: 'carrier' is an out-dated term indicating the 'provider' for parcel delivery and flights.
        departureGate: Identifier of the flight's departure gate.
        seller: An entity which offers (sells / leases / lends / loans) the services / goods.  A seller may also be a provider.
        arrivalTerminal: Identifier of the flight's arrival terminal.
        flightDistance: The distance of the flight.
        webCheckinTime: The time when a passenger can check into the flight online.
        mealService: Description of the meals that will be provided or available for purchase.
        aircraft: The kind of aircraft (e.g., "Boeing 747").
        arrivalGate: Identifier of the flight's arrival gate.
        flightNumber: The unique identifier for a flight including the airline IATA code. For example, if describing United flight 110, where the IATA code for United is 'UA', the flightNumber is 'UA110'.
        departureTerminal: Identifier of the flight's departure terminal.
        arrivalAirport: The airport where the flight terminates.
    '''
    class_: Literal['https://schema.org/Flight'] = Field( # type: ignore
        default='https://schema.org/Flight',
        alias='@type',
        serialization_alias='@type'
    )
    boardingPolicy: Optional[Union['BoardingPolicyType', List['BoardingPolicyType']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    estimatedFlightDuration: Optional[Union[str, List[str], 'Duration', List['Duration']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    departureAirport: Optional[Union['Airport', List['Airport']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    carrier: Optional[Union['Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    departureGate: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    seller: Optional[Union['Organization', List['Organization'], 'Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    arrivalTerminal: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    flightDistance: Optional[Union[str, List[str], 'Distance', List['Distance']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    webCheckinTime: Optional[Union[datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    mealService: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    aircraft: Optional[Union['Vehicle', List['Vehicle'], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    arrivalGate: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    flightNumber: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    departureTerminal: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    arrivalAirport: Optional[Union['Airport', List['Airport']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
