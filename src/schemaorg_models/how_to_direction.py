from typing import Union, List, Optional
from pydantic import field_serializer, AliasChoices, Field, HttpUrl
from schemaorg_models.creative_work import CreativeWork

from schemaorg_models.media_object import MediaObject

class HowToDirection(CreativeWork):
    """
A direction indicating a single action to do in the instructions for how to achieve a result.
    """
    beforeMedia: Optional[Union[MediaObject, List[MediaObject], HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('beforeMedia', 'https://schema.org/beforeMedia'),serialization_alias='https://schema.org/beforeMedia')
    @field_serializer('beforeMedia')
    def beforeMedia2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    prepTime: Optional[Union["Duration", List["Duration"]]] = Field(default=None,validation_alias=AliasChoices('prepTime', 'https://schema.org/prepTime'),serialization_alias='https://schema.org/prepTime')
    supply: Optional[Union["HowToSupply", List["HowToSupply"], str, List[str]]] = Field(default=None,validation_alias=AliasChoices('supply', 'https://schema.org/supply'),serialization_alias='https://schema.org/supply')
    performTime: Optional[Union["Duration", List["Duration"]]] = Field(default=None,validation_alias=AliasChoices('performTime', 'https://schema.org/performTime'),serialization_alias='https://schema.org/performTime')
    totalTime: Optional[Union["Duration", List["Duration"]]] = Field(default=None,validation_alias=AliasChoices('totalTime', 'https://schema.org/totalTime'),serialization_alias='https://schema.org/totalTime')
    duringMedia: Optional[Union[HttpUrl, List[HttpUrl], MediaObject, List[MediaObject]]] = Field(default=None,validation_alias=AliasChoices('duringMedia', 'https://schema.org/duringMedia'),serialization_alias='https://schema.org/duringMedia')
    @field_serializer('duringMedia')
    def duringMedia2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    tool: Optional[Union[str, List[str], "HowToTool", List["HowToTool"]]] = Field(default=None,validation_alias=AliasChoices('tool', 'https://schema.org/tool'),serialization_alias='https://schema.org/tool')
    afterMedia: Optional[Union[HttpUrl, List[HttpUrl], MediaObject, List[MediaObject]]] = Field(default=None,validation_alias=AliasChoices('afterMedia', 'https://schema.org/afterMedia'),serialization_alias='https://schema.org/afterMedia')
    @field_serializer('afterMedia')
    def afterMedia2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

