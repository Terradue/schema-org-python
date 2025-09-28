from __future__ import annotations

from .local_business import LocalBusiness    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class SelfStorage(LocalBusiness):
    """
A self-storage facility.
    """
    class_: Literal['https://schema.org/SelfStorage'] = Field( # type: ignore
        default='https://schema.org/SelfStorage',
        alias='@type',
        serialization_alias='@type'
    )
