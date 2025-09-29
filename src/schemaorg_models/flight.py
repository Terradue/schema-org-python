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
    from .organization import Organization
    from .airport import Airport
    from .duration import Duration
    from .distance import Distance
    from .boarding_policy_type import BoardingPolicyType
    from .person import Person

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
            'boardingPolicy',
            'https://schema.org/boardingPolicy'
        ),
        serialization_alias='https://schema.org/boardingPolicy'
    )
    estimatedFlightDuration: Optional[Union[str, List[str], 'Duration', List['Duration']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'estimatedFlightDuration',
            'https://schema.org/estimatedFlightDuration'
        ),
        serialization_alias='https://schema.org/estimatedFlightDuration'
    )
    departureAirport: Optional[Union['Airport', List['Airport']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'departureAirport',
            'https://schema.org/departureAirport'
        ),
        serialization_alias='https://schema.org/departureAirport'
    )
    carrier: Optional[Union['Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'carrier',
            'https://schema.org/carrier'
        ),
        serialization_alias='https://schema.org/carrier'
    )
    departureGate: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'departureGate',
            'https://schema.org/departureGate'
        ),
        serialization_alias='https://schema.org/departureGate'
    )
    seller: Optional[Union['Organization', List['Organization'], 'Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'seller',
            'https://schema.org/seller'
        ),
        serialization_alias='https://schema.org/seller'
    )
    arrivalTerminal: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'arrivalTerminal',
            'https://schema.org/arrivalTerminal'
        ),
        serialization_alias='https://schema.org/arrivalTerminal'
    )
    flightDistance: Optional[Union[str, List[str], 'Distance', List['Distance']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'flightDistance',
            'https://schema.org/flightDistance'
        ),
        serialization_alias='https://schema.org/flightDistance'
    )
    webCheckinTime: Optional[Union[datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'webCheckinTime',
            'https://schema.org/webCheckinTime'
        ),
        serialization_alias='https://schema.org/webCheckinTime'
    )
    mealService: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'mealService',
            'https://schema.org/mealService'
        ),
        serialization_alias='https://schema.org/mealService'
    )
    aircraft: Optional[Union['Vehicle', List['Vehicle'], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'aircraft',
            'https://schema.org/aircraft'
        ),
        serialization_alias='https://schema.org/aircraft'
    )
    arrivalGate: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'arrivalGate',
            'https://schema.org/arrivalGate'
        ),
        serialization_alias='https://schema.org/arrivalGate'
    )
    flightNumber: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'flightNumber',
            'https://schema.org/flightNumber'
        ),
        serialization_alias='https://schema.org/flightNumber'
    )
    departureTerminal: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'departureTerminal',
            'https://schema.org/departureTerminal'
        ),
        serialization_alias='https://schema.org/departureTerminal'
    )
    arrivalAirport: Optional[Union['Airport', List['Airport']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'arrivalAirport',
            'https://schema.org/arrivalAirport'
        ),
        serialization_alias='https://schema.org/arrivalAirport'
    )
