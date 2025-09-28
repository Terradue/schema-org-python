from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.educational_organization import EducationalOrganization

from pydantic import (
    Field
)
from typing import (
    Literal
)

class Preschool(EducationalOrganization):
    """
A preschool.
    """
    class_: Literal['https://schema.org/Preschool'] = Field( # type: ignore
        default='https://schema.org/Preschool',
        alias='@type',
        serialization_alias='@type'
    )
