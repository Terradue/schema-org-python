from __future__ import annotations

from .store import Store    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class HobbyShop(Store):
    """
A store that sells materials useful or necessary for various hobbies.
    """
    class_: Literal['https://schema.org/HobbyShop'] = Field( # type: ignore
        default='https://schema.org/HobbyShop',
        alias='@type',
        serialization_alias='@type'
    )
