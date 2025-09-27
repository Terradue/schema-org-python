from typing import Literal
from pydantic import Field
from schemaorg_models.reservation import Reservation


class EventReservation(Reservation):
    """
A reservation for an event like a concert, sporting event, or lecture.\
\
Note: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations. For offers of tickets, use [[Offer]].
    """
    class_: Literal['https://schema.org/EventReservation'] = Field(default='https://schema.org/EventReservation', alias='class', serialization_alias='class') # type: ignore
