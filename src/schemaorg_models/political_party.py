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

class PoliticalParty(Organization):
    """
Organization: Political Party.
    """
    class_: Literal['https://schema.org/PoliticalParty'] = Field( # type: ignore
        default='https://schema.org/PoliticalParty',
        alias='@type',
        serialization_alias='@type'
    )
