from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.enumeration import Enumeration


class EventAttendanceModeEnumeration(Enumeration):
    """
An EventAttendanceModeEnumeration value is one of potentially several modes of organising an event, relating to whether it is online or offline.
    """
    type_: Literal['https://schema.org/EventAttendanceModeEnumeration'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/EventAttendanceModeEnumeration'),serialization_alias='class') # type: ignore
