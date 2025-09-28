from __future__ import annotations

from .enumeration import Enumeration    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class DayOfWeek(Enumeration):
    """
The day of the week for which these opening hours are valid.
    """
    class_: Literal['https://schema.org/DayOfWeek'] = Field( # type: ignore
        default='https://schema.org/DayOfWeek',
        alias='@type',
        serialization_alias='@type'
    )
