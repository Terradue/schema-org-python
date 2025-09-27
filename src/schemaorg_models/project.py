from typing import Literal
from pydantic import Field
from schemaorg_models.organization import Organization


class Project(Organization):
    """
An enterprise (potentially individual but typically collaborative), planned to achieve a particular aim.
Use properties from [[Organization]], [[subOrganization]]/[[parentOrganization]] to indicate project sub-structures. 
   
    """
    type_: Literal['https://schema.org/Project'] = Field(default='https://schema.org/Project', alias='@type', serialization_alias='@type') # type: ignore
