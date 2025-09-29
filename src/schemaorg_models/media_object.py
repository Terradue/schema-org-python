from __future__ import annotations
from datetime import (
    date,
    datetime,
    time
)
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
from .creative_work import CreativeWork
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .claim import Claim
    from .quantitative_value import QuantitativeValue
    from .duration import Duration
    from .news_article import NewsArticle
    from .media_subscription import MediaSubscription
    from .geo_shape import GeoShape
    from .organization import Organization
    from .distance import Distance
    from .place import Place

class MediaObject(CreativeWork):
    """
A media object, such as an image, video, audio, or text object embedded in a web page or a downloadable dataset i.e. DataDownload. Note that a creative work may have many media objects associated with it on the same web page. For example, a page about a single song (MusicRecording) may have a music video (VideoObject), and a high and low bandwidth audio stream (2 AudioObject's).
    """
    class_: Literal['https://schema.org/MediaObject'] = Field( # type: ignore
        default='https://schema.org/MediaObject',
        alias='@type',
        serialization_alias='@type'
    )
    encodesCreativeWork: Optional[Union["CreativeWork", List["CreativeWork"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'encodesCreativeWork',
            'https://schema.org/encodesCreativeWork'
        ),
        serialization_alias='https://schema.org/encodesCreativeWork'
    )
    height: Optional[Union["Distance", List["Distance"], "QuantitativeValue", List["QuantitativeValue"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'height',
            'https://schema.org/height'
        ),
        serialization_alias='https://schema.org/height'
    )
    productionCompany: Optional[Union["Organization", List["Organization"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'productionCompany',
            'https://schema.org/productionCompany'
        ),
        serialization_alias='https://schema.org/productionCompany'
    )
    regionsAllowed: Optional[Union["Place", List["Place"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'regionsAllowed',
            'https://schema.org/regionsAllowed'
        ),
        serialization_alias='https://schema.org/regionsAllowed'
    )
    contentSize: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'contentSize',
            'https://schema.org/contentSize'
        ),
        serialization_alias='https://schema.org/contentSize'
    )
    interpretedAsClaim: Optional[Union["Claim", List["Claim"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'interpretedAsClaim',
            'https://schema.org/interpretedAsClaim'
        ),
        serialization_alias='https://schema.org/interpretedAsClaim'
    )
    requiresSubscription: Optional[Union[bool, List[bool], "MediaSubscription", List["MediaSubscription"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'requiresSubscription',
            'https://schema.org/requiresSubscription'
        ),
        serialization_alias='https://schema.org/requiresSubscription'
    )
    endTime: Optional[Union[time, List[time], datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'endTime',
            'https://schema.org/endTime'
        ),
        serialization_alias='https://schema.org/endTime'
    )
    bitrate: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'bitrate',
            'https://schema.org/bitrate'
        ),
        serialization_alias='https://schema.org/bitrate'
    )
    encodingFormat: Optional[Union[HttpUrl, List[HttpUrl], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'encodingFormat',
            'https://schema.org/encodingFormat'
        ),
        serialization_alias='https://schema.org/encodingFormat'
    )
    contentUrl: Optional[Union[HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'contentUrl',
            'https://schema.org/contentUrl'
        ),
        serialization_alias='https://schema.org/contentUrl'
    )
    associatedArticle: Optional[Union["NewsArticle", List["NewsArticle"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'associatedArticle',
            'https://schema.org/associatedArticle'
        ),
        serialization_alias='https://schema.org/associatedArticle'
    )
    width: Optional[Union["QuantitativeValue", List["QuantitativeValue"], "Distance", List["Distance"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'width',
            'https://schema.org/width'
        ),
        serialization_alias='https://schema.org/width'
    )
    playerType: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'playerType',
            'https://schema.org/playerType'
        ),
        serialization_alias='https://schema.org/playerType'
    )
    duration: Optional[Union["Duration", List["Duration"], "QuantitativeValue", List["QuantitativeValue"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'duration',
            'https://schema.org/duration'
        ),
        serialization_alias='https://schema.org/duration'
    )
    embedUrl: Optional[Union[HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'embedUrl',
            'https://schema.org/embedUrl'
        ),
        serialization_alias='https://schema.org/embedUrl'
    )
    startTime: Optional[Union[time, List[time], datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'startTime',
            'https://schema.org/startTime'
        ),
        serialization_alias='https://schema.org/startTime'
    )
    ineligibleRegion: Optional[Union[str, List[str], "Place", List["Place"], "GeoShape", List["GeoShape"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'ineligibleRegion',
            'https://schema.org/ineligibleRegion'
        ),
        serialization_alias='https://schema.org/ineligibleRegion'
    )
    sha256: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'sha256',
            'https://schema.org/sha256'
        ),
        serialization_alias='https://schema.org/sha256'
    )
    uploadDate: Optional[Union[date, List[date], datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'uploadDate',
            'https://schema.org/uploadDate'
        ),
        serialization_alias='https://schema.org/uploadDate'
    )
