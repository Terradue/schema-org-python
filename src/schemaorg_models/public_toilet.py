from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .civic_structure import CivicStructure

class PublicToilet(CivicStructure):
    """
A public toilet is a room or small building containing one or more toilets (and possibly also urinals) which is available for use by the general public, or by customers or employees of certain businesses.
    """
    class_: Literal['https://schema.org/PublicToilet'] = Field( # type: ignore
        default='https://schema.org/PublicToilet',
        alias='@type',
        serialization_alias='@type'
    )
