from __future__ import annotations

from .local_business import LocalBusiness    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class InternetCafe(LocalBusiness):
    """
An internet cafe.
    """
    class_: Literal['https://schema.org/InternetCafe'] = Field( # type: ignore
        default='https://schema.org/InternetCafe',
        alias='@type',
        serialization_alias='@type'
    )
