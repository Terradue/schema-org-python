from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.residence import Residence

from pydantic import (
    Field
)
from typing import (
    Literal
)

class GatedResidenceCommunity(Residence):
    """
Residence type: Gated community.
    """
    class_: Literal['https://schema.org/GatedResidenceCommunity'] = Field( # type: ignore
        default='https://schema.org/GatedResidenceCommunity',
        alias='@type',
        serialization_alias='@type'
    )
