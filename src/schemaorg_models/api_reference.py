from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.tech_article import TechArticle

from pydantic import (
    AliasChoices,
    Field
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)

class APIReference(TechArticle):
    """
Reference documentation for application programming interfaces (APIs).
    """
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
