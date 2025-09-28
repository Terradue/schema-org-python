from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.reservation import Reservation

from pydantic import (
    Field
)
from typing import (
    Literal
)

class BusReservation(Reservation):
    """
A reservation for bus travel. \
\
Note: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations. For offers of tickets, use [[Offer]].
    """
    class_: Literal['https://schema.org/BusReservation'] = Field( # type: ignore
        default='https://schema.org/BusReservation',
        alias='@type',
        serialization_alias='@type'
    )
