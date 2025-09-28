from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .anatomical_structure import AnatomicalStructure

class Vessel(AnatomicalStructure):
    """
A component of the human body circulatory system comprised of an intricate network of hollow tubes that transport blood throughout the entire body.
    """
    class_: Literal['https://schema.org/Vessel'] = Field( # type: ignore
        default='https://schema.org/Vessel',
        alias='@type',
        serialization_alias='@type'
    )
