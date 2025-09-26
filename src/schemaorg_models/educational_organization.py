from typing import Union, List, Optional
from pydantic import AliasChoices, Field
from schemaorg_models.civic_structure import CivicStructure

from schemaorg_models.person import Person

class EducationalOrganization(CivicStructure):
    """
An educational organization.
    """
    alumni: Optional[Union[Person, List[Person]]] = Field(default=None,validation_alias=AliasChoices('alumni', 'https://schema.org/alumni'),serialization_alias='https://schema.org/alumni')
