from typing import Literal
from pydantic import Field
from schemaorg_models.status_enumeration import StatusEnumeration


class ReservationStatusType(StatusEnumeration):
    """
Enumerated status values for Reservation.
    """
    class_: Literal['https://schema.org/ReservationStatusType'] = Field('class', alias='class', serialization_alias='class') # type: ignore
