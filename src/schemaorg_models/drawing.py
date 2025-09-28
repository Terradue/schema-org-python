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

class Drawing(CreativeWork):
    """
A picture or diagram made with a pencil, pen, or crayon rather than paint.
    """
    class_: Literal['https://schema.org/Drawing'] = Field( # type: ignore
        default='https://schema.org/Drawing',
        alias='@type',
        serialization_alias='@type'
    )
