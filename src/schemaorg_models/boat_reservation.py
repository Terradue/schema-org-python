from typing import Literal
from pydantic import Field
from schemaorg_models.reservation import Reservation


class BoatReservation(Reservation):
    """
A reservation for boat travel.

Note: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations. For offers of tickets, use [[Offer]].
    """
    class_: Literal['https://schema.org/BoatReservation'] = Field(default='https://schema.org/BoatReservation', alias='class', serialization_alias='class') # type: ignore
