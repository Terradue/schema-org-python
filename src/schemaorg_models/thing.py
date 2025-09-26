from typing import Union, List, Optional
from pydantic import field_serializer, AliasChoices, Field, HttpUrl


from pydantic import BaseModel
class Thing(BaseModel):
    """
The most generic type of item.
    """
    additionalType: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('additionalType', 'https://schema.org/additionalType'),serialization_alias='https://schema.org/additionalType')
    @field_serializer('additionalType')
    def additionalType2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    identifier: Optional[Union[HttpUrl, List[HttpUrl], str, List[str], "PropertyValue", List["PropertyValue"]]] = Field(default=None,validation_alias=AliasChoices('identifier', 'https://schema.org/identifier'),serialization_alias='https://schema.org/identifier')
    @field_serializer('identifier')
    def identifier2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    image: Optional[Union["ImageObject", List["ImageObject"], HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('image', 'https://schema.org/image'),serialization_alias='https://schema.org/image')
    @field_serializer('image')
    def image2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    url: Optional[Union[HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('url', 'https://schema.org/url'),serialization_alias='https://schema.org/url')
    @field_serializer('url')
    def url2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    disambiguatingDescription: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('disambiguatingDescription', 'https://schema.org/disambiguatingDescription'),serialization_alias='https://schema.org/disambiguatingDescription')
    description: Optional[Union[str, List[str], "TextObject", List["TextObject"]]] = Field(default=None,validation_alias=AliasChoices('description', 'https://schema.org/description'),serialization_alias='https://schema.org/description')
    mainEntityOfPage: Optional[Union["CreativeWork", List["CreativeWork"], HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('mainEntityOfPage', 'https://schema.org/mainEntityOfPage'),serialization_alias='https://schema.org/mainEntityOfPage')
    @field_serializer('mainEntityOfPage')
    def mainEntityOfPage2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    sameAs: Optional[Union[HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('sameAs', 'https://schema.org/sameAs'),serialization_alias='https://schema.org/sameAs')
    @field_serializer('sameAs')
    def sameAs2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    name: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('name', 'https://schema.org/name'),serialization_alias='https://schema.org/name')
    subjectOf: Optional[Union["Event", List["Event"], "CreativeWork", List["CreativeWork"]]] = Field(default=None,validation_alias=AliasChoices('subjectOf', 'https://schema.org/subjectOf'),serialization_alias='https://schema.org/subjectOf')
    alternateName: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('alternateName', 'https://schema.org/alternateName'),serialization_alias='https://schema.org/alternateName')
    potentialAction: Optional[Union["Action", List["Action"]]] = Field(default=None,validation_alias=AliasChoices('potentialAction', 'https://schema.org/potentialAction'),serialization_alias='https://schema.org/potentialAction')
