from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.reservation import Reservation


class BoatReservation(Reservation):
    """
A reservation for boat travel.

Note: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations. For offers of tickets, use [[Offer]].
    """
    type_: Literal['https://schema.org/BoatReservation'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/BoatReservation'),serialization_alias='class') # type: ignore
