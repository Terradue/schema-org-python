from typing import Union, List, Optional
from pydantic import AliasChoices, Field
from schemaorg_models.role import Role


class PerformanceRole(Role):
    """
A PerformanceRole is a Role that some entity places with regard to a theatrical performance, e.g. in a Movie, TVSeries etc.
    """
    characterName: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('characterName', 'https://schema.org/characterName'),serialization_alias='https://schema.org/characterName')
