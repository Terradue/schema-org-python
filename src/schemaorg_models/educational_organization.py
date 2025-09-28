from __future__ import annotations

from .civic_structure import CivicStructure    

from pydantic import (
    AliasChoices,
    Field
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from schemaorg_models.person import Person

class EducationalOrganization(CivicStructure):
    """
An educational organization.
    """
    class_: Literal['https://schema.org/EducationalOrganization'] = Field( # type: ignore
        default='https://schema.org/EducationalOrganization',
        alias='@type',
        serialization_alias='@type'
    )
    alumni: Optional[Union[Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'alumni',
            'https://schema.org/alumni'
        ),
        serialization_alias='https://schema.org/alumni'
    )
