from typing import List, Literal, Optional, Union
from pydantic import field_serializer, AliasChoices, Field, HttpUrl
from schemaorg_models.creative_work import CreativeWork

from schemaorg_models.person import Person

class VisualArtwork(CreativeWork):
    """
A work of art that is primarily visual in character.
    """
    type_: Literal['https://schema.org/VisualArtwork'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/VisualArtwork'),serialization_alias='class') # type: ignore
    weight: Optional[Union["QuantitativeValue", List["QuantitativeValue"], "Mass", List["Mass"]]] = Field(default=None,validation_alias=AliasChoices('weight', 'https://schema.org/weight'),serialization_alias='https://schema.org/weight')
    artworkSurface: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('artworkSurface', 'https://schema.org/artworkSurface'),serialization_alias='https://schema.org/artworkSurface')
    @field_serializer('artworkSurface')
    def artworkSurface2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    colorist: Optional[Union[Person, List[Person]]] = Field(default=None,validation_alias=AliasChoices('colorist', 'https://schema.org/colorist'),serialization_alias='https://schema.org/colorist')
    artist: Optional[Union[Person, List[Person]]] = Field(default=None,validation_alias=AliasChoices('artist', 'https://schema.org/artist'),serialization_alias='https://schema.org/artist')
    penciler: Optional[Union[Person, List[Person]]] = Field(default=None,validation_alias=AliasChoices('penciler', 'https://schema.org/penciler'),serialization_alias='https://schema.org/penciler')
    depth: Optional[Union["Distance", List["Distance"], "QuantitativeValue", List["QuantitativeValue"]]] = Field(default=None,validation_alias=AliasChoices('depth', 'https://schema.org/depth'),serialization_alias='https://schema.org/depth')
    surface: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('surface', 'https://schema.org/surface'),serialization_alias='https://schema.org/surface')
    @field_serializer('surface')
    def surface2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    artEdition: Optional[Union[str, List[str], int, List[int]]] = Field(default=None,validation_alias=AliasChoices('artEdition', 'https://schema.org/artEdition'),serialization_alias='https://schema.org/artEdition')
    width: Optional[Union["QuantitativeValue", List["QuantitativeValue"], "Distance", List["Distance"]]] = Field(default=None,validation_alias=AliasChoices('width', 'https://schema.org/width'),serialization_alias='https://schema.org/width')
    artMedium: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('artMedium', 'https://schema.org/artMedium'),serialization_alias='https://schema.org/artMedium')
    @field_serializer('artMedium')
    def artMedium2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    artform: Optional[Union[HttpUrl, List[HttpUrl], str, List[str]]] = Field(default=None,validation_alias=AliasChoices('artform', 'https://schema.org/artform'),serialization_alias='https://schema.org/artform')
    @field_serializer('artform')
    def artform2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    inker: Optional[Union[Person, List[Person]]] = Field(default=None,validation_alias=AliasChoices('inker', 'https://schema.org/inker'),serialization_alias='https://schema.org/inker')
    letterer: Optional[Union[Person, List[Person]]] = Field(default=None,validation_alias=AliasChoices('letterer', 'https://schema.org/letterer'),serialization_alias='https://schema.org/letterer')
    height: Optional[Union["Distance", List["Distance"], "QuantitativeValue", List["QuantitativeValue"]]] = Field(default=None,validation_alias=AliasChoices('height', 'https://schema.org/height'),serialization_alias='https://schema.org/height')
