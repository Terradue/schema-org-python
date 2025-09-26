from typing import Union, List, Optional
from pydantic import AliasChoices, Field
from schemaorg_models.role import Role


class OrganizationRole(Role):
    """
A subclass of Role used to describe roles within organizations.
    """
    numberedPosition: Optional[Union[float, List[float]]] = Field(default=None,validation_alias=AliasChoices('numberedPosition', 'https://schema.org/numberedPosition'),serialization_alias='https://schema.org/numberedPosition')
