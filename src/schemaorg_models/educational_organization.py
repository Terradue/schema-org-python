from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.civic_structure import CivicStructure

from schemaorg_models.person import Person

class EducationalOrganization(CivicStructure):
    """
An educational organization.
    """
    class_: Literal['https://schema.org/EducationalOrganization'] = Field(default='https://schema.org/EducationalOrganization', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
    alumni: Optional[Union[Person, List[Person]]] = Field(default=None, validation_alias=AliasChoices('alumni', 'https://schema.org/alumni'), serialization_alias='https://schema.org/alumni')
