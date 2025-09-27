from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.role import Role


class OrganizationRole(Role):
    """
A subclass of Role used to describe roles within organizations.
    """
    type_: Literal['https://schema.org/OrganizationRole'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/OrganizationRole'),serialization_alias='class') # type: ignore
    numberedPosition: Optional[Union[float, List[float]]] = Field(default=None,validation_alias=AliasChoices('numberedPosition', 'https://schema.org/numberedPosition'),serialization_alias='https://schema.org/numberedPosition')
