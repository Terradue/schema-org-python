from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .intangible import Intangible

class _Class(Intangible):
    """
A class, also often called a 'Type'; equivalent to rdfs:Class.
    """
    class_: Literal['https://schema.org/_Class'] = Field( # type: ignore
        default='https://schema.org/_Class',
        alias='@type',
        serialization_alias='@type'
    )
