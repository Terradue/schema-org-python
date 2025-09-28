from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.creative_work import CreativeWork

from pydantic import (
    Field
)
from typing import (
    Literal
)

class Photograph(CreativeWork):
    """
A photograph.
    """
    class_: Literal['https://schema.org/Photograph'] = Field( # type: ignore
        default='https://schema.org/Photograph',
        alias='@type',
        serialization_alias='@type'
    )
