from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.landform import Landform

from pydantic import (
    Field
)
from typing import (
    Literal
)

class Mountain(Landform):
    """
A mountain, like Mount Whitney or Mount Everest.
    """
    class_: Literal['https://schema.org/Mountain'] = Field( # type: ignore
        default='https://schema.org/Mountain',
        alias='@type',
        serialization_alias='@type'
    )
