from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.organization import Organization

from pydantic import (
    Field
)
from typing import (
    Literal
)

class PerformingGroup(Organization):
    """
A performance group, such as a band, an orchestra, or a circus.
    """
    class_: Literal['https://schema.org/PerformingGroup'] = Field( # type: ignore
        default='https://schema.org/PerformingGroup',
        alias='@type',
        serialization_alias='@type'
    )
