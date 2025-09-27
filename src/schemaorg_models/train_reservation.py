from typing import Literal
from pydantic import Field
from schemaorg_models.reservation import Reservation


class TrainReservation(Reservation):
    """
A reservation for train travel.\
\
Note: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations. For offers of tickets, use [[Offer]].
    """
    type_: Literal['https://schema.org/TrainReservation'] = Field(default='https://schema.org/TrainReservation', alias='@type', serialization_alias='@type') # type: ignore
