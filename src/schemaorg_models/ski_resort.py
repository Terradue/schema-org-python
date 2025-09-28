from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.resort import Resort

from pydantic import (
    Field
)
from typing import (
    Literal
)

class SkiResort(Resort):
    """
A ski resort.
    """
    class_: Literal['https://schema.org/SkiResort'] = Field( # type: ignore
        default='https://schema.org/SkiResort',
        alias='@type',
        serialization_alias='@type'
    )
