from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .local_business import LocalBusiness

class DryCleaningOrLaundry(LocalBusiness):
    """
A dry-cleaning business.
    """
    class_: Literal['https://schema.org/DryCleaningOrLaundry'] = Field( # type: ignore
        default='https://schema.org/DryCleaningOrLaundry',
        alias='@type',
        serialization_alias='@type'
    )
