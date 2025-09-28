from __future__ import annotations

from .organization import Organization    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class Cooperative(Organization):
    """
An organization that is a joint project of multiple organizations or persons.
    """
    class_: Literal['https://schema.org/Cooperative'] = Field( # type: ignore
        default='https://schema.org/Cooperative',
        alias='@type',
        serialization_alias='@type'
    )
