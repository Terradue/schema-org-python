from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .local_business import LocalBusiness

class InternetCafe(LocalBusiness):
    """
An internet cafe.
    """
    class_: Literal['https://schema.org/InternetCafe'] = Field( # type: ignore
        default='https://schema.org/InternetCafe',
        alias='@type',
        serialization_alias='@type'
    )
