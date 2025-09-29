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
            'assembly',
            'https://schema.org/assembly'
        ),
        serialization_alias='https://schema.org/assembly'
    )
    targetPlatform: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'targetPlatform',
            'https://schema.org/targetPlatform'
        ),
        serialization_alias='https://schema.org/targetPlatform'
    )
    executableLibraryName: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'executableLibraryName',
            'https://schema.org/executableLibraryName'
        ),
        serialization_alias='https://schema.org/executableLibraryName'
    )
    assemblyVersion: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'assemblyVersion',
            'https://schema.org/assemblyVersion'
        ),
        serialization_alias='https://schema.org/assemblyVersion'
    )
    programmingModel: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'programmingModel',
            'https://schema.org/programmingModel'
        ),
        serialization_alias='https://schema.org/programmingModel'
    )
