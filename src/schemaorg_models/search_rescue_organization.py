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

class SearchRescueOrganization(Organization):
    """
A Search and Rescue organization of some kind.
    """
    class_: Literal['https://schema.org/SearchRescueOrganization'] = Field( # type: ignore
        default='https://schema.org/SearchRescueOrganization',
        alias='@type',
        serialization_alias='@type'
    )
