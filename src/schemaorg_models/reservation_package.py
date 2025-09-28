from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.reservation import Reservation

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

class ReservationPackage(Reservation):
    """
A group of multiple reservations with common values for all sub-reservations.
    """
    class_: Literal['https://schema.org/ReservationPackage'] = Field( # type: ignore
        default='https://schema.org/ReservationPackage',
        alias='@type',
        serialization_alias='@type'
    )
    subReservation: Optional[Union[Reservation, List[Reservation]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'subReservation',
            'https://schema.org/subReservation'
        ),
        serialization_alias='https://schema.org/subReservation'
    )
