from __future__ import annotations

from .local_business import LocalBusiness    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class TouristInformationCenter(LocalBusiness):
    """
A tourist information center.
    """
    class_: Literal['https://schema.org/TouristInformationCenter'] = Field( # type: ignore
        default='https://schema.org/TouristInformationCenter',
        alias='@type',
        serialization_alias='@type'
    )
