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

class HowToTip(CreativeWork):
    """
An explanation in the instructions for how to achieve a result. It provides supplementary information about a technique, supply, author's preference, etc. It can explain what could be done, or what should not be done, but doesn't specify what should be done (see HowToDirection).
    """
    class_: Literal['https://schema.org/HowToTip'] = Field( # type: ignore
        default='https://schema.org/HowToTip',
        alias='@type',
        serialization_alias='@type'
    )
