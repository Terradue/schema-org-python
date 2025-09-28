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

class BrainStructure(AnatomicalStructure):
    """
Any anatomical structure which pertains to the soft nervous tissue functioning as the coordinating center of sensation and intellectual and nervous activity.
    """
    class_: Literal['https://schema.org/BrainStructure'] = Field( # type: ignore
        default='https://schema.org/BrainStructure',
        alias='@type',
        serialization_alias='@type'
    )
