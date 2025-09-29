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
from .creative_work import CreativeWork
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .image_object import ImageObject
    from .data_feed import DataFeed

class SoftwareApplication(CreativeWork):
    '''
    A software application.

    Attributes:
        applicationCategory: Type of software application, e.g. 'Game, Multimedia'.
        requirements: Component dependency requirements for application. This includes runtime environments and shared libraries that are not included in the application distribution package, but required to run the application (examples: DirectX, Java or .NET runtime).
        memoryRequirements: Minimum memory requirements.
        countriesNotSupported: Countries for which the application is not supported. You can also provide the two-letter ISO 3166-1 alpha-2 country code.
        permissions: Permission(s) required to run the app (for example, a mobile app may require full internet access or may run only on wifi).
        processorRequirements: Processor architecture required to run the application (e.g. IA64).
        installUrl: URL at which the app may be installed, if different from the URL of the item.
        applicationSubCategory: Subcategory of the application, e.g. 'Arcade Game'.
        downloadUrl: If the file can be downloaded, URL to download the binary.
        releaseNotes: Description of what changed in this version.
        availableOnDevice: Device required to run the application. Used in cases where a specific make/model is required to run the application.
        softwareHelp: Software application help.
        softwareRequirements: Component dependency requirements for application. This includes runtime environments and shared libraries that are not included in the application distribution package, but required to run the application (examples: DirectX, Java or .NET runtime).
        featureList: Features or modules provided by this application (and possibly required by other applications).
        supportingData: Supporting data for a SoftwareApplication.
        fileSize: Size of the application / package (e.g. 18MB). In the absence of a unit (MB, KB etc.), KB will be assumed.
        storageRequirements: Storage requirements (free space required).
        device: Device required to run the application. Used in cases where a specific make/model is required to run the application.
        countriesSupported: Countries for which the application is supported. You can also provide the two-letter ISO 3166-1 alpha-2 country code.
        operatingSystem: Operating systems supported (Windows 7, OS X 10.6, Android 1.6).
        screenshot: A link to a screenshot image of the app.
        softwareAddOn: Additional content for a software application.
        softwareVersion: Version of the software instance.
        applicationSuite: The name of the application suite to which the application belongs (e.g. Excel belongs to Office).
    '''
    class_: Literal['https://schema.org/SoftwareApplication'] = Field( # type: ignore
        default='https://schema.org/SoftwareApplication',
        alias='@type',
        serialization_alias='@type'
    )
    applicationCategory: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'applicationCategory',
            'https://schema.org/applicationCategory'
        ),
        serialization_alias='https://schema.org/applicationCategory'
    )
    requirements: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'requirements',
            'https://schema.org/requirements'
        ),
        serialization_alias='https://schema.org/requirements'
    )
    memoryRequirements: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'memoryRequirements',
            'https://schema.org/memoryRequirements'
        ),
        serialization_alias='https://schema.org/memoryRequirements'
    )
    countriesNotSupported: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'countriesNotSupported',
            'https://schema.org/countriesNotSupported'
        ),
        serialization_alias='https://schema.org/countriesNotSupported'
    )
    permissions: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'permissions',
            'https://schema.org/permissions'
        ),
        serialization_alias='https://schema.org/permissions'
    )
    processorRequirements: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'processorRequirements',
            'https://schema.org/processorRequirements'
        ),
        serialization_alias='https://schema.org/processorRequirements'
    )
    installUrl: Optional[Union[HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'installUrl',
            'https://schema.org/installUrl'
        ),
        serialization_alias='https://schema.org/installUrl'
    )
    applicationSubCategory: Optional[Union[HttpUrl, List[HttpUrl], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'applicationSubCategory',
            'https://schema.org/applicationSubCategory'
        ),
        serialization_alias='https://schema.org/applicationSubCategory'
    )
    downloadUrl: Optional[Union[HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'downloadUrl',
            'https://schema.org/downloadUrl'
        ),
        serialization_alias='https://schema.org/downloadUrl'
    )
    releaseNotes: Optional[Union[HttpUrl, List[HttpUrl], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'releaseNotes',
            'https://schema.org/releaseNotes'
        ),
        serialization_alias='https://schema.org/releaseNotes'
    )
    availableOnDevice: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'availableOnDevice',
            'https://schema.org/availableOnDevice'
        ),
        serialization_alias='https://schema.org/availableOnDevice'
    )
    softwareHelp: Optional[Union['CreativeWork', List['CreativeWork']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'softwareHelp',
            'https://schema.org/softwareHelp'
        ),
        serialization_alias='https://schema.org/softwareHelp'
    )
    softwareRequirements: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'softwareRequirements',
            'https://schema.org/softwareRequirements'
        ),
        serialization_alias='https://schema.org/softwareRequirements'
    )
    featureList: Optional[Union[HttpUrl, List[HttpUrl], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'featureList',
            'https://schema.org/featureList'
        ),
        serialization_alias='https://schema.org/featureList'
    )
    supportingData: Optional[Union['DataFeed', List['DataFeed']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'supportingData',
            'https://schema.org/supportingData'
        ),
        serialization_alias='https://schema.org/supportingData'
    )
    fileSize: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'fileSize',
            'https://schema.org/fileSize'
        ),
        serialization_alias='https://schema.org/fileSize'
    )
    storageRequirements: Optional[Union[HttpUrl, List[HttpUrl], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'storageRequirements',
            'https://schema.org/storageRequirements'
        ),
        serialization_alias='https://schema.org/storageRequirements'
    )
    device: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'device',
            'https://schema.org/device'
        ),
        serialization_alias='https://schema.org/device'
    )
    countriesSupported: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'countriesSupported',
            'https://schema.org/countriesSupported'
        ),
        serialization_alias='https://schema.org/countriesSupported'
    )
    operatingSystem: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'operatingSystem',
            'https://schema.org/operatingSystem'
        ),
        serialization_alias='https://schema.org/operatingSystem'
    )
    screenshot: Optional[Union[HttpUrl, List[HttpUrl], 'ImageObject', List['ImageObject']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'screenshot',
            'https://schema.org/screenshot'
        ),
        serialization_alias='https://schema.org/screenshot'
    )
    softwareAddOn: Optional[Union['SoftwareApplication', List['SoftwareApplication']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'softwareAddOn',
            'https://schema.org/softwareAddOn'
        ),
        serialization_alias='https://schema.org/softwareAddOn'
    )
    softwareVersion: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'softwareVersion',
            'https://schema.org/softwareVersion'
        ),
        serialization_alias='https://schema.org/softwareVersion'
    )
    applicationSuite: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'applicationSuite',
            'https://schema.org/applicationSuite'
        ),
        serialization_alias='https://schema.org/applicationSuite'
    )
