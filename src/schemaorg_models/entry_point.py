from typing import List, Literal, Optional, Union
from pydantic import field_serializer, AliasChoices, Field, HttpUrl
from schemaorg_models.intangible import Intangible


class EntryPoint(Intangible):
    """
An entry point, within some Web-based protocol.
    """
    type_: Literal['https://schema.org/EntryPoint'] = Field(default='https://schema.org/EntryPoint', alias='@type', serialization_alias='@type') # type: ignore
    httpMethod: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('httpMethod', 'https://schema.org/httpMethod'), serialization_alias='https://schema.org/httpMethod')
    contentType: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('contentType', 'https://schema.org/contentType'), serialization_alias='https://schema.org/contentType')
    urlTemplate: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('urlTemplate', 'https://schema.org/urlTemplate'), serialization_alias='https://schema.org/urlTemplate')
    actionApplication: Optional[Union["SoftwareApplication", List["SoftwareApplication"]]] = Field(default=None, validation_alias=AliasChoices('actionApplication', 'https://schema.org/actionApplication'), serialization_alias='https://schema.org/actionApplication')
    encodingType: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('encodingType', 'https://schema.org/encodingType'), serialization_alias='https://schema.org/encodingType')
    application: Optional[Union["SoftwareApplication", List["SoftwareApplication"]]] = Field(default=None, validation_alias=AliasChoices('application', 'https://schema.org/application'), serialization_alias='https://schema.org/application')
    actionPlatform: Optional[Union[str, List[str], HttpUrl, List[HttpUrl], "DigitalPlatformEnumeration", List["DigitalPlatformEnumeration"]]] = Field(default=None, validation_alias=AliasChoices('actionPlatform', 'https://schema.org/actionPlatform'), serialization_alias='https://schema.org/actionPlatform')
    @field_serializer('actionPlatform')
    def actionPlatform2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

