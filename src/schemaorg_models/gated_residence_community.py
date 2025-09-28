from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .residence import Residence

class GatedResidenceCommunity(Residence):
    """
Residence type: Gated community.
    """
    class_: Literal['https://schema.org/GatedResidenceCommunity'] = Field( # type: ignore
        default='https://schema.org/GatedResidenceCommunity',
        alias='@type',
        serialization_alias='@type'
    )
