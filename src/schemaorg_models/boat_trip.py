from __future__ import annotations
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
from .trip import Trip
from .boat_terminal import BoatTerminal

class BoatTrip(Trip):
    """
A trip on a commercial ferry line.
    """
    class_: Literal['https://schema.org/BoatTrip'] = Field( # type: ignore
        default='https://schema.org/BoatTrip',
        alias='@type',
        serialization_alias='@type'
    )
    departureBoatTerminal: Optional[Union[BoatTerminal, List[BoatTerminal]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'departureBoatTerminal',
            'https://schema.org/departureBoatTerminal'
        ),
        serialization_alias='https://schema.org/departureBoatTerminal'
    )
    arrivalBoatTerminal: Optional[Union[BoatTerminal, List[BoatTerminal]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'arrivalBoatTerminal',
            'https://schema.org/arrivalBoatTerminal'
        ),
        serialization_alias='https://schema.org/arrivalBoatTerminal'
    )
