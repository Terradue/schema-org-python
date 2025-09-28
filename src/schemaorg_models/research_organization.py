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

class ResearchOrganization(Organization):
    """
A Research Organization (e.g. scientific institute, research company).
    """
    class_: Literal['https://schema.org/ResearchOrganization'] = Field( # type: ignore
        default='https://schema.org/ResearchOrganization',
        alias='@type',
        serialization_alias='@type'
    )
