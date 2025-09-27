from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.reservation import Reservation


class EventReservation(Reservation):
    """
A reservation for an event like a concert, sporting event, or lecture.\
\
Note: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations. For offers of tickets, use [[Offer]].
    """
    type_: Literal['https://schema.org/EventReservation'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/EventReservation'),serialization_alias='class') # type: ignore
