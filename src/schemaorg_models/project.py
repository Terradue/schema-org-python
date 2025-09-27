from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.organization import Organization


class Project(Organization):
    """
An enterprise (potentially individual but typically collaborative), planned to achieve a particular aim.
Use properties from [[Organization]], [[subOrganization]]/[[parentOrganization]] to indicate project sub-structures. 
   
    """
    type_: Literal['https://schema.org/Project'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Project'),serialization_alias='class') # type: ignore
