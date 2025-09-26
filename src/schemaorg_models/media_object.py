from typing import Union, List, Optional
from datetime import date, datetime, time
from pydantic import field_serializer, AliasChoices, Field, HttpUrl
from schemaorg_models.creative_work import CreativeWork

from schemaorg_models.creative_work import CreativeWork
from schemaorg_models.organization import Organization
from schemaorg_models.place import Place
from schemaorg_models.media_subscription import MediaSubscription

class MediaObject(CreativeWork):
    """
A media object, such as an image, video, audio, or text object embedded in a web page or a downloadable dataset i.e. DataDownload. Note that a creative work may have many media objects associated with it on the same web page. For example, a page about a single song (MusicRecording) may have a music video (VideoObject), and a high and low bandwidth audio stream (2 AudioObject's).
    """
    encodesCreativeWork: Optional[Union[CreativeWork, List[CreativeWork]]] = Field(default=None,validation_alias=AliasChoices('encodesCreativeWork', 'https://schema.org/encodesCreativeWork'),serialization_alias='https://schema.org/encodesCreativeWork')
    height: Optional[Union["Distance", List["Distance"], "QuantitativeValue", List["QuantitativeValue"]]] = Field(default=None,validation_alias=AliasChoices('height', 'https://schema.org/height'),serialization_alias='https://schema.org/height')
    productionCompany: Optional[Union[Organization, List[Organization]]] = Field(default=None,validation_alias=AliasChoices('productionCompany', 'https://schema.org/productionCompany'),serialization_alias='https://schema.org/productionCompany')
    regionsAllowed: Optional[Union[Place, List[Place]]] = Field(default=None,validation_alias=AliasChoices('regionsAllowed', 'https://schema.org/regionsAllowed'),serialization_alias='https://schema.org/regionsAllowed')
    contentSize: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('contentSize', 'https://schema.org/contentSize'),serialization_alias='https://schema.org/contentSize')
    interpretedAsClaim: Optional[Union["Claim", List["Claim"]]] = Field(default=None,validation_alias=AliasChoices('interpretedAsClaim', 'https://schema.org/interpretedAsClaim'),serialization_alias='https://schema.org/interpretedAsClaim')
    requiresSubscription: Optional[Union[bool, List[bool], MediaSubscription, List[MediaSubscription]]] = Field(default=None,validation_alias=AliasChoices('requiresSubscription', 'https://schema.org/requiresSubscription'),serialization_alias='https://schema.org/requiresSubscription')
    endTime: Optional[Union[time, List[time], datetime, List[datetime]]] = Field(default=None,validation_alias=AliasChoices('endTime', 'https://schema.org/endTime'),serialization_alias='https://schema.org/endTime')
    bitrate: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('bitrate', 'https://schema.org/bitrate'),serialization_alias='https://schema.org/bitrate')
    encodingFormat: Optional[Union[HttpUrl, List[HttpUrl], str, List[str]]] = Field(default=None,validation_alias=AliasChoices('encodingFormat', 'https://schema.org/encodingFormat'),serialization_alias='https://schema.org/encodingFormat')
    @field_serializer('encodingFormat')
    def encodingFormat2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    contentUrl: Optional[Union[HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('contentUrl', 'https://schema.org/contentUrl'),serialization_alias='https://schema.org/contentUrl')
    @field_serializer('contentUrl')
    def contentUrl2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    associatedArticle: Optional[Union["NewsArticle", List["NewsArticle"]]] = Field(default=None,validation_alias=AliasChoices('associatedArticle', 'https://schema.org/associatedArticle'),serialization_alias='https://schema.org/associatedArticle')
    width: Optional[Union["QuantitativeValue", List["QuantitativeValue"], "Distance", List["Distance"]]] = Field(default=None,validation_alias=AliasChoices('width', 'https://schema.org/width'),serialization_alias='https://schema.org/width')
    playerType: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('playerType', 'https://schema.org/playerType'),serialization_alias='https://schema.org/playerType')
    duration: Optional[Union["Duration", List["Duration"], "QuantitativeValue", List["QuantitativeValue"]]] = Field(default=None,validation_alias=AliasChoices('duration', 'https://schema.org/duration'),serialization_alias='https://schema.org/duration')
    embedUrl: Optional[Union[HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('embedUrl', 'https://schema.org/embedUrl'),serialization_alias='https://schema.org/embedUrl')
    @field_serializer('embedUrl')
    def embedUrl2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    startTime: Optional[Union[time, List[time], datetime, List[datetime]]] = Field(default=None,validation_alias=AliasChoices('startTime', 'https://schema.org/startTime'),serialization_alias='https://schema.org/startTime')
    ineligibleRegion: Optional[Union[str, List[str], Place, List[Place], "GeoShape", List["GeoShape"]]] = Field(default=None,validation_alias=AliasChoices('ineligibleRegion', 'https://schema.org/ineligibleRegion'),serialization_alias='https://schema.org/ineligibleRegion')
    sha256: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('sha256', 'https://schema.org/sha256'),serialization_alias='https://schema.org/sha256')
    uploadDate: Optional[Union[date, List[date], datetime, List[datetime]]] = Field(default=None,validation_alias=AliasChoices('uploadDate', 'https://schema.org/uploadDate'),serialization_alias='https://schema.org/uploadDate')
