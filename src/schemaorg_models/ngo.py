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

class NGO(Organization):
    """
Organization: Non-governmental Organization.
    """
    class_: Literal['https://schema.org/NGO'] = Field( # type: ignore
        default='https://schema.org/NGO',
        alias='@type',
        serialization_alias='@type'
    )
