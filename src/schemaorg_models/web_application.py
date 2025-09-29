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
from .software_application import SoftwareApplication

class WebApplication(SoftwareApplication):
    '''
    Web applications.

    Attributes:
        browserRequirements: Specifies browser requirements in human-readable text. For example, 'requires HTML5 support'.
    '''
    class_: Literal['https://schema.org/WebApplication'] = Field( # type: ignore
        default='https://schema.org/WebApplication',
        alias='@type',
        serialization_alias='@type'
    )
    browserRequirements: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
