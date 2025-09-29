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
from .tech_article import TechArticle

class APIReference(TechArticle):
    '''
    Reference documentation for application programming interfaces (APIs).

    Attributes:
        assembly: Library file name, e.g., mscorlib.dll, system.web.dll.
        targetPlatform: Type of app development: phone, Metro style, desktop, XBox, etc.
        executableLibraryName: Library file name, e.g., mscorlib.dll, system.web.dll.
        assemblyVersion: Associated product/technology version. E.g., .NET Framework 4.5.
        programmingModel: Indicates whether API is managed or unmanaged.
    '''
    class_: Literal['https://schema.org/APIReference'] = Field( # type: ignore
        default='https://schema.org/APIReference',
        alias='@type',
        serialization_alias='@type'
    )
    assembly: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    targetPlatform: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    executableLibraryName: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    assemblyVersion: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    programmingModel: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
