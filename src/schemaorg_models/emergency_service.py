from __future__ import annotations

from .local_business import LocalBusiness    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class EmergencyService(LocalBusiness):
    """
An emergency service, such as a fire station or ER.
    """
    class_: Literal['https://schema.org/EmergencyService'] = Field( # type: ignore
        default='https://schema.org/EmergencyService',
        alias='@type',
        serialization_alias='@type'
    )
