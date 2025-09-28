from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .organization import Organization

class Cooperative(Organization):
    """
An organization that is a joint project of multiple organizations or persons.
    """
    class_: Literal['https://schema.org/Cooperative'] = Field( # type: ignore
        default='https://schema.org/Cooperative',
        alias='@type',
        serialization_alias='@type'
    )
