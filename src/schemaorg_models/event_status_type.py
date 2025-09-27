from typing import Literal
from pydantic import Field
from schemaorg_models.status_enumeration import StatusEnumeration


class EventStatusType(StatusEnumeration):
    """
EventStatusType is an enumeration type whose instances represent several states that an Event may be in.
    """
    type_: Literal['https://schema.org/EventStatusType'] = Field(default='https://schema.org/EventStatusType', alias='@type', serialization_alias='@type') # type: ignore
