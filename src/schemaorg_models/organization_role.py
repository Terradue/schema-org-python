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

class OrganizationRole(Role):
    '''
    A subclass of Role used to describe roles within organizations.

    Attributes:
        numberedPosition: A number associated with a role in an organization, for example, the number on an athlete's jersey.
    '''
    class_: Literal['https://schema.org/OrganizationRole'] = Field( # type: ignore
        default='https://schema.org/OrganizationRole',
        alias='@type',
        serialization_alias='@type'
    )
    numberedPosition: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'numberedPosition',
            'https://schema.org/numberedPosition'
        ),
        serialization_alias='https://schema.org/numberedPosition'
    )
