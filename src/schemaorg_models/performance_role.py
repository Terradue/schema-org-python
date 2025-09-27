from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.role import Role


class PerformanceRole(Role):
    """
A PerformanceRole is a Role that some entity places with regard to a theatrical performance, e.g. in a Movie, TVSeries etc.
    """
    class_: Literal['https://schema.org/PerformanceRole'] = Field(default='https://schema.org/PerformanceRole', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
    characterName: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('characterName', 'https://schema.org/characterName'), serialization_alias='https://schema.org/characterName')
