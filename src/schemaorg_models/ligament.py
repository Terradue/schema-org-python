from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.anatomical_structure import AnatomicalStructure

from pydantic import (
    Field
)
from typing import (
    Literal
)

class Ligament(AnatomicalStructure):
    """
A short band of tough, flexible, fibrous connective tissue that functions to connect multiple bones, cartilages, and structurally support joints.
    """
    class_: Literal['https://schema.org/Ligament'] = Field( # type: ignore
        default='https://schema.org/Ligament',
        alias='@type',
        serialization_alias='@type'
    )
