from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.reservation import Reservation

from schemaorg_models.reservation import Reservation

class ReservationPackage(Reservation):
    """
A group of multiple reservations with common values for all sub-reservations.
    """
    class_: Literal['https://schema.org/ReservationPackage'] = Field('class', alias='class', serialization_alias='class') # type: ignore
    subReservation: Optional[Union[Reservation, List[Reservation]]] = Field(default=None,validation_alias=AliasChoices('subReservation', 'https://schema.org/subReservation'), serialization_alias='https://schema.org/subReservation')
