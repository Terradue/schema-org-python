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
from .intangible import Intangible
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .digital_platform_enumeration import DigitalPlatformEnumeration
    from .software_application import SoftwareApplication

class EntryPoint(Intangible):
    '''
    An entry point, within some Web-based protocol.

    Attributes:
        httpMethod: An HTTP method that specifies the appropriate HTTP method for a request to an HTTP EntryPoint. Values are capitalized strings as used in HTTP.
        contentType: The supported content type(s) for an EntryPoint response.
        urlTemplate: An url template (RFC6570) that will be used to construct the target of the execution of the action.
        actionApplication: An application that can complete the request.
        encodingType: The supported encoding type(s) for an EntryPoint request.
        application: An application that can complete the request.
        actionPlatform: The high level platform(s) where the Action can be performed for the given URL. To specify a specific application or operating system instance, use actionApplication.
    '''
    class_: Literal['https://schema.org/EntryPoint'] = Field( # type: ignore
        default='https://schema.org/EntryPoint',
        alias='@type',
        serialization_alias='@type'
    )
    httpMethod: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    contentType: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    urlTemplate: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    actionApplication: Optional[Union['SoftwareApplication', List['SoftwareApplication']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    encodingType: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    application: Optional[Union['SoftwareApplication', List['SoftwareApplication']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    actionPlatform: Optional[Union[str, List[str], HttpUrl, List[HttpUrl], 'DigitalPlatformEnumeration', List['DigitalPlatformEnumeration']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
