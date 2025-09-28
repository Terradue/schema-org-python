from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.status_enumeration import StatusEnumeration

from pydantic import (
    Field
)
from typing import (
    Literal
)

class EventStatusType(StatusEnumeration):
    """
EventStatusType is an enumeration type whose instances represent several states that an Event may be in.
    """
    class_: Literal['https://schema.org/EventStatusType'] = Field( # type: ignore
        default='https://schema.org/EventStatusType',
        alias='@type',
        serialization_alias='@type'
    )
