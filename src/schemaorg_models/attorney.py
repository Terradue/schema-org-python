from __future__ import annotations

from .legal_service import LegalService    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class Attorney(LegalService):
    """
Professional service: Attorney. \
\
This type is deprecated - [[LegalService]] is more inclusive and less ambiguous.
    """
    class_: Literal['https://schema.org/Attorney'] = Field( # type: ignore
        default='https://schema.org/Attorney',
        alias='@type',
        serialization_alias='@type'
    )
