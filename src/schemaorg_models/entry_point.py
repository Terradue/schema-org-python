from __future__ import annotations
from pydantic import (
    AliasChoices,
    Field,
    HttpUrl
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .intangible import Intangible
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .software_application import SoftwareApplication
    from .digital_platform_enumeration import DigitalPlatformEnumeration

class EntryPoint(Intangible):
    """
An entry point, within some Web-based protocol.
    """
    class_: Literal['https://schema.org/EntryPoint'] = Field( # type: ignore
        default='https://schema.org/EntryPoint',
        alias='@type',
        serialization_alias='@type'
    )
    httpMethod: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'httpMethod',
            'https://schema.org/httpMethod'
        ),
        serialization_alias='https://schema.org/httpMethod'
    )
    contentType: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'contentType',
            'https://schema.org/contentType'
        ),
        serialization_alias='https://schema.org/contentType'
    )
    urlTemplate: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'urlTemplate',
            'https://schema.org/urlTemplate'
        ),
        serialization_alias='https://schema.org/urlTemplate'
    )
    actionApplication: Optional[Union["SoftwareApplication", List["SoftwareApplication"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'actionApplication',
            'https://schema.org/actionApplication'
        ),
        serialization_alias='https://schema.org/actionApplication'
    )
    encodingType: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'encodingType',
            'https://schema.org/encodingType'
        ),
        serialization_alias='https://schema.org/encodingType'
    )
    application: Optional[Union["SoftwareApplication", List["SoftwareApplication"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'application',
            'https://schema.org/application'
        ),
        serialization_alias='https://schema.org/application'
    )
    actionPlatform: Optional[Union[str, List[str], HttpUrl, List[HttpUrl], "DigitalPlatformEnumeration", List["DigitalPlatformEnumeration"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'actionPlatform',
            'https://schema.org/actionPlatform'
        ),
        serialization_alias='https://schema.org/actionPlatform'
    )
