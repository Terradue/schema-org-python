from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.reservation import Reservation

from schemaorg_models.reservation import Reservation

class ReservationPackage(Reservation):
    """
A group of multiple reservations with common values for all sub-reservations.
    """
    class_: Literal['https://schema.org/ReservationPackage'] = Field(default='https://schema.org/ReservationPackage', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
    subReservation: Optional[Union[Reservation, List[Reservation]]] = Field(default=None, validation_alias=AliasChoices('subReservation', 'https://schema.org/subReservation'), serialization_alias='https://schema.org/subReservation')
