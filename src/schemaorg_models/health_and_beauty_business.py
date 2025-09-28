from __future__ import annotations

from .local_business import LocalBusiness    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class HealthAndBeautyBusiness(LocalBusiness):
    """
Health and beauty.
    """
    class_: Literal['https://schema.org/HealthAndBeautyBusiness'] = Field( # type: ignore
        default='https://schema.org/HealthAndBeautyBusiness',
        alias='@type',
        serialization_alias='@type'
    )
