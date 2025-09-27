from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.status_enumeration import StatusEnumeration


class ReservationStatusType(StatusEnumeration):
    """
Enumerated status values for Reservation.
    """
    type_: Literal['https://schema.org/ReservationStatusType'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/ReservationStatusType'),serialization_alias='class') # type: ignore
