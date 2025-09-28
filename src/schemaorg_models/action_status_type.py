from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .status_enumeration import StatusEnumeration

class ActionStatusType(StatusEnumeration):
    """
The status of an Action.
    """
    class_: Literal['https://schema.org/ActionStatusType'] = Field( # type: ignore
        default='https://schema.org/ActionStatusType',
        alias='@type',
        serialization_alias='@type'
    )
