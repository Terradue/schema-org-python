from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .organization import Organization

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
