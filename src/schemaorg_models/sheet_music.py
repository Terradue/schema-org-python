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

class SheetMusic(CreativeWork):
    """
Printed music, as opposed to performed or recorded music.
    """
    class_: Literal['https://schema.org/SheetMusic'] = Field( # type: ignore
        default='https://schema.org/SheetMusic',
        alias='@type',
        serialization_alias='@type'
    )
