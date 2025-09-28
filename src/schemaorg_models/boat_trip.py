from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.trip import Trip

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
from schemaorg_models.boat_terminal import BoatTerminal

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
