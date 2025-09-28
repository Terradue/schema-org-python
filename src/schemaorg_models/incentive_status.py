from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .enumeration import Enumeration

class IncentiveStatus(Enumeration):
    """
Enumerates a status for an incentive, such as whether it is active.
    """
    class_: Literal['https://schema.org/IncentiveStatus'] = Field( # type: ignore
        default='https://schema.org/IncentiveStatus',
        alias='@type',
        serialization_alias='@type'
    )
