from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.status_enumeration import StatusEnumeration


class EventStatusType(StatusEnumeration):
    """
EventStatusType is an enumeration type whose instances represent several states that an Event may be in.
    """
    type_: Literal['https://schema.org/EventStatusType'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/EventStatusType'),serialization_alias='class') # type: ignore
