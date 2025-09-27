from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.role import Role


class PerformanceRole(Role):
    """
A PerformanceRole is a Role that some entity places with regard to a theatrical performance, e.g. in a Movie, TVSeries etc.
    """
    type_: Literal['https://schema.org/PerformanceRole'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/PerformanceRole'),serialization_alias='class') # type: ignore
    characterName: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('characterName', 'https://schema.org/characterName'),serialization_alias='https://schema.org/characterName')
