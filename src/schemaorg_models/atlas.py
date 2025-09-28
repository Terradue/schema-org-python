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

class Atlas(CreativeWork):
    """
A collection or bound volume of maps, charts, plates or tables, physical or in media form illustrating any subject.
    """
    class_: Literal['https://schema.org/Atlas'] = Field( # type: ignore
        default='https://schema.org/Atlas',
        alias='@type',
        serialization_alias='@type'
    )
