from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.civic_structure import CivicStructure

from schemaorg_models.person import Person

class EducationalOrganization(CivicStructure):
    """
An educational organization.
    """
    type_: Literal['https://schema.org/EducationalOrganization'] = Field(default='https://schema.org/EducationalOrganization', alias='@type', serialization_alias='@type') # type: ignore
    alumni: Optional[Union[Person, List[Person]]] = Field(default=None, validation_alias=AliasChoices('alumni', 'https://schema.org/alumni'), serialization_alias='https://schema.org/alumni')
