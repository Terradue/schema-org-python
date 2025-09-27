from typing import Literal
from pydantic import Field
from schemaorg_models.status_enumeration import StatusEnumeration


class EventStatusType(StatusEnumeration):
    """
EventStatusType is an enumeration type whose instances represent several states that an Event may be in.
    """
    class_: Literal['https://schema.org/EventStatusType'] = Field('class', alias='class', serialization_alias='class') # type: ignore
