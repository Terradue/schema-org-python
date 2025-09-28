from __future__ import annotations

from .status_enumeration import StatusEnumeration    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class ActionStatusType(StatusEnumeration):
    """
The status of an Action.
    """
    class_: Literal['https://schema.org/ActionStatusType'] = Field( # type: ignore
        default='https://schema.org/ActionStatusType',
        alias='@type',
        serialization_alias='@type'
    )
