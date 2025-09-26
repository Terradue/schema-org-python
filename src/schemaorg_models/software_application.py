from typing import Union, List, Optional
from pydantic import AliasChoices, Field, HttpUrl
from schemaorg_models.creative_work import CreativeWork

from schemaorg_models.creative_work import CreativeWork

class SoftwareApplication(CreativeWork):
    """
A software application.
    """
    applicationCategory: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('applicationCategory', 'https://schema.org/applicationCategory'),serialization_alias='https://schema.org/applicationCategory')
    requirements: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('requirements', 'https://schema.org/requirements'),serialization_alias='https://schema.org/requirements')
    memoryRequirements: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('memoryRequirements', 'https://schema.org/memoryRequirements'),serialization_alias='https://schema.org/memoryRequirements')
    countriesNotSupported: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('countriesNotSupported', 'https://schema.org/countriesNotSupported'),serialization_alias='https://schema.org/countriesNotSupported')
    permissions: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('permissions', 'https://schema.org/permissions'),serialization_alias='https://schema.org/permissions')
    processorRequirements: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('processorRequirements', 'https://schema.org/processorRequirements'),serialization_alias='https://schema.org/processorRequirements')
    installUrl: Optional[Union[HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('installUrl', 'https://schema.org/installUrl'),serialization_alias='https://schema.org/installUrl')
    applicationSubCategory: Optional[Union[HttpUrl, List[HttpUrl], str, List[str]]] = Field(default=None,validation_alias=AliasChoices('applicationSubCategory', 'https://schema.org/applicationSubCategory'),serialization_alias='https://schema.org/applicationSubCategory')
    downloadUrl: Optional[Union[HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('downloadUrl', 'https://schema.org/downloadUrl'),serialization_alias='https://schema.org/downloadUrl')
    releaseNotes: Optional[Union[HttpUrl, List[HttpUrl], str, List[str]]] = Field(default=None,validation_alias=AliasChoices('releaseNotes', 'https://schema.org/releaseNotes'),serialization_alias='https://schema.org/releaseNotes')
    availableOnDevice: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('availableOnDevice', 'https://schema.org/availableOnDevice'),serialization_alias='https://schema.org/availableOnDevice')
    softwareHelp: Optional[Union[CreativeWork, List[CreativeWork]]] = Field(default=None,validation_alias=AliasChoices('softwareHelp', 'https://schema.org/softwareHelp'),serialization_alias='https://schema.org/softwareHelp')
    softwareRequirements: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('softwareRequirements', 'https://schema.org/softwareRequirements'),serialization_alias='https://schema.org/softwareRequirements')
    featureList: Optional[Union[HttpUrl, List[HttpUrl], str, List[str]]] = Field(default=None,validation_alias=AliasChoices('featureList', 'https://schema.org/featureList'),serialization_alias='https://schema.org/featureList')
    supportingData: Optional[Union["DataFeed", List["DataFeed"]]] = Field(default=None,validation_alias=AliasChoices('supportingData', 'https://schema.org/supportingData'),serialization_alias='https://schema.org/supportingData')
    fileSize: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('fileSize', 'https://schema.org/fileSize'),serialization_alias='https://schema.org/fileSize')
    storageRequirements: Optional[Union[HttpUrl, List[HttpUrl], str, List[str]]] = Field(default=None,validation_alias=AliasChoices('storageRequirements', 'https://schema.org/storageRequirements'),serialization_alias='https://schema.org/storageRequirements')
    device: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('device', 'https://schema.org/device'),serialization_alias='https://schema.org/device')
    countriesSupported: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('countriesSupported', 'https://schema.org/countriesSupported'),serialization_alias='https://schema.org/countriesSupported')
    operatingSystem: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('operatingSystem', 'https://schema.org/operatingSystem'),serialization_alias='https://schema.org/operatingSystem')
    screenshot: Optional[Union[HttpUrl, List[HttpUrl], "ImageObject", List["ImageObject"]]] = Field(default=None,validation_alias=AliasChoices('screenshot', 'https://schema.org/screenshot'),serialization_alias='https://schema.org/screenshot')
    softwareAddOn: Optional[Union["SoftwareApplication", List["SoftwareApplication"]]] = Field(default=None,validation_alias=AliasChoices('softwareAddOn', 'https://schema.org/softwareAddOn'),serialization_alias='https://schema.org/softwareAddOn')
    softwareVersion: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('softwareVersion', 'https://schema.org/softwareVersion'),serialization_alias='https://schema.org/softwareVersion')
    applicationSuite: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('applicationSuite', 'https://schema.org/applicationSuite'),serialization_alias='https://schema.org/applicationSuite')
