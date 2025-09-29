from __future__ import annotations
from datetime import (
    date,
    datetime,
    time
)
from pydantic import (
    field_serializer,
    field_validator,
    AliasChoices,
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .role import Role

class PerformanceRole(Role):
    '''
    A PerformanceRole is a Role that some entity places with regard to a theatrical performance, e.g. in a Movie, TVSeries etc.

    Attributes:
        characterName: The name of a character played in some acting or performing role, i.e. in a PerformanceRole.
    '''
    class_: Literal['https://schema.org/PerformanceRole'] = Field( # type: ignore
        default='https://schema.org/PerformanceRole',
        alias='@type',
        serialization_alias='@type'
    )
    characterName: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'characterName',
            'https://schema.org/characterName'
        ),
        serialization_alias='https://schema.org/characterName'
    )
