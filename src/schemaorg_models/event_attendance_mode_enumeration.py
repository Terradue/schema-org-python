from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class EventAttendanceModeEnumeration(Enumeration):
    """
An EventAttendanceModeEnumeration value is one of potentially several modes of organising an event, relating to whether it is online or offline.
    """
    type_: Literal['https://schema.org/EventAttendanceModeEnumeration'] = Field(default='https://schema.org/EventAttendanceModeEnumeration', alias='@type', serialization_alias='@type') # type: ignore
