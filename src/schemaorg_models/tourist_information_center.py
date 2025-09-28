from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .local_business import LocalBusiness

class TouristInformationCenter(LocalBusiness):
    """
A tourist information center.
    """
    class_: Literal['https://schema.org/TouristInformationCenter'] = Field( # type: ignore
        default='https://schema.org/TouristInformationCenter',
        alias='@type',
        serialization_alias='@type'
    )
