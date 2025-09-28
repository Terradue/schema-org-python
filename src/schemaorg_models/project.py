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

class Project(Organization):
    """
An enterprise (potentially individual but typically collaborative), planned to achieve a particular aim.
Use properties from [[Organization]], [[subOrganization]]/[[parentOrganization]] to indicate project sub-structures. 
   
    """
    class_: Literal['https://schema.org/Project'] = Field( # type: ignore
        default='https://schema.org/Project',
        alias='@type',
        serialization_alias='@type'
    )
