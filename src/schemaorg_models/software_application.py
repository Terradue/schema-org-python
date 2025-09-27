from typing import List, Literal, Optional, Union
from pydantic import field_serializer, AliasChoices, Field, HttpUrl
from schemaorg_models.creative_work import CreativeWork

from schemaorg_models.creative_work import CreativeWork

class SoftwareApplication(CreativeWork):
    """
A software application.
    """
    class_: Literal['https://schema.org/SoftwareApplication'] = Field(default='https://schema.org/SoftwareApplication', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
    applicationCategory: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = Field(default=None, validation_alias=AliasChoices('applicationCategory', 'https://schema.org/applicationCategory'), serialization_alias='https://schema.org/applicationCategory')
    @field_serializer('applicationCategory')
    def applicationCategory2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    requirements: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = Field(default=None, validation_alias=AliasChoices('requirements', 'https://schema.org/requirements'), serialization_alias='https://schema.org/requirements')
    @field_serializer('requirements')
    def requirements2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    memoryRequirements: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = Field(default=None, validation_alias=AliasChoices('memoryRequirements', 'https://schema.org/memoryRequirements'), serialization_alias='https://schema.org/memoryRequirements')
    @field_serializer('memoryRequirements')
    def memoryRequirements2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    countriesNotSupported: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('countriesNotSupported', 'https://schema.org/countriesNotSupported'), serialization_alias='https://schema.org/countriesNotSupported')
    permissions: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('permissions', 'https://schema.org/permissions'), serialization_alias='https://schema.org/permissions')
    processorRequirements: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('processorRequirements', 'https://schema.org/processorRequirements'), serialization_alias='https://schema.org/processorRequirements')
    installUrl: Optional[Union[HttpUrl, List[HttpUrl]]] = Field(default=None, validation_alias=AliasChoices('installUrl', 'https://schema.org/installUrl'), serialization_alias='https://schema.org/installUrl')
    @field_serializer('installUrl')
    def installUrl2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    applicationSubCategory: Optional[Union[HttpUrl, List[HttpUrl], str, List[str]]] = Field(default=None, validation_alias=AliasChoices('applicationSubCategory', 'https://schema.org/applicationSubCategory'), serialization_alias='https://schema.org/applicationSubCategory')
    @field_serializer('applicationSubCategory')
    def applicationSubCategory2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    downloadUrl: Optional[Union[HttpUrl, List[HttpUrl]]] = Field(default=None, validation_alias=AliasChoices('downloadUrl', 'https://schema.org/downloadUrl'), serialization_alias='https://schema.org/downloadUrl')
    @field_serializer('downloadUrl')
    def downloadUrl2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    releaseNotes: Optional[Union[HttpUrl, List[HttpUrl], str, List[str]]] = Field(default=None, validation_alias=AliasChoices('releaseNotes', 'https://schema.org/releaseNotes'), serialization_alias='https://schema.org/releaseNotes')
    @field_serializer('releaseNotes')
    def releaseNotes2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    availableOnDevice: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('availableOnDevice', 'https://schema.org/availableOnDevice'), serialization_alias='https://schema.org/availableOnDevice')
    softwareHelp: Optional[Union[CreativeWork, List[CreativeWork]]] = Field(default=None, validation_alias=AliasChoices('softwareHelp', 'https://schema.org/softwareHelp'), serialization_alias='https://schema.org/softwareHelp')
    softwareRequirements: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = Field(default=None, validation_alias=AliasChoices('softwareRequirements', 'https://schema.org/softwareRequirements'), serialization_alias='https://schema.org/softwareRequirements')
    @field_serializer('softwareRequirements')
    def softwareRequirements2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    featureList: Optional[Union[HttpUrl, List[HttpUrl], str, List[str]]] = Field(default=None, validation_alias=AliasChoices('featureList', 'https://schema.org/featureList'), serialization_alias='https://schema.org/featureList')
    @field_serializer('featureList')
    def featureList2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    supportingData: Optional[Union["DataFeed", List["DataFeed"]]] = Field(default=None, validation_alias=AliasChoices('supportingData', 'https://schema.org/supportingData'), serialization_alias='https://schema.org/supportingData')
    fileSize: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('fileSize', 'https://schema.org/fileSize'), serialization_alias='https://schema.org/fileSize')
    storageRequirements: Optional[Union[HttpUrl, List[HttpUrl], str, List[str]]] = Field(default=None, validation_alias=AliasChoices('storageRequirements', 'https://schema.org/storageRequirements'), serialization_alias='https://schema.org/storageRequirements')
    @field_serializer('storageRequirements')
    def storageRequirements2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    device: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('device', 'https://schema.org/device'), serialization_alias='https://schema.org/device')
    countriesSupported: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('countriesSupported', 'https://schema.org/countriesSupported'), serialization_alias='https://schema.org/countriesSupported')
    operatingSystem: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('operatingSystem', 'https://schema.org/operatingSystem'), serialization_alias='https://schema.org/operatingSystem')
    screenshot: Optional[Union[HttpUrl, List[HttpUrl], "ImageObject", List["ImageObject"]]] = Field(default=None, validation_alias=AliasChoices('screenshot', 'https://schema.org/screenshot'), serialization_alias='https://schema.org/screenshot')
    @field_serializer('screenshot')
    def screenshot2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    softwareAddOn: Optional[Union["SoftwareApplication", List["SoftwareApplication"]]] = Field(default=None, validation_alias=AliasChoices('softwareAddOn', 'https://schema.org/softwareAddOn'), serialization_alias='https://schema.org/softwareAddOn')
    softwareVersion: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('softwareVersion', 'https://schema.org/softwareVersion'), serialization_alias='https://schema.org/softwareVersion')
    applicationSuite: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('applicationSuite', 'https://schema.org/applicationSuite'), serialization_alias='https://schema.org/applicationSuite')
