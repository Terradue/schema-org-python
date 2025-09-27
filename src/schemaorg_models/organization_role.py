from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.role import Role


class OrganizationRole(Role):
    """
A subclass of Role used to describe roles within organizations.
    """
    class_: Literal['https://schema.org/OrganizationRole'] = Field(default='https://schema.org/OrganizationRole', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
    numberedPosition: Optional[Union[float, List[float]]] = Field(default=None, validation_alias=AliasChoices('numberedPosition', 'https://schema.org/numberedPosition'), serialization_alias='https://schema.org/numberedPosition')
