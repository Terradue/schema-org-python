from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .government_office import GovernmentOffice

class PostOffice(GovernmentOffice):
    """
A post office.
    """
    class_: Literal['https://schema.org/PostOffice'] = Field( # type: ignore
        default='https://schema.org/PostOffice',
        alias='@type',
        serialization_alias='@type'
    )
