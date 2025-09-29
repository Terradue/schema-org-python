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
    from .geo_shape import GeoShape
    from .quantitative_value import QuantitativeValue
    from .media_subscription import MediaSubscription
    from .organization import Organization
    from .place import Place
    from .distance import Distance
    from .duration import Duration
    from .claim import Claim
    from .news_article import NewsArticle

class MediaObject(CreativeWork):
    '''
    A media object, such as an image, video, audio, or text object embedded in a web page or a downloadable dataset i.e. DataDownload. Note that a creative work may have many media objects associated with it on the same web page. For example, a page about a single song (MusicRecording) may have a music video (VideoObject), and a high and low bandwidth audio stream (2 AudioObject's).

    Attributes:
        encodesCreativeWork: The CreativeWork encoded by this media object.
        height: The height of the item.
        productionCompany: The production company or studio responsible for the item, e.g. series, video game, episode etc.
        regionsAllowed: The regions where the media is allowed. If not specified, then it's assumed to be allowed everywhere. Specify the countries in [ISO 3166 format](http://en.wikipedia.org/wiki/ISO_3166).
        contentSize: File size in (mega/kilo)bytes.
        interpretedAsClaim: Used to indicate a specific claim contained, implied, translated or refined from the content of a [[MediaObject]] or other [[CreativeWork]]. The interpreting party can be indicated using [[claimInterpreter]].
        requiresSubscription: Indicates if use of the media require a subscription  (either paid or free). Allowed values are ```true``` or ```false``` (note that an earlier version had 'yes', 'no').
        endTime: The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. E.g. John wrote a book from January to *December*. For media, including audio and video, it's the time offset of the end of a clip within a larger file.\
\
Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions.
        bitrate: The bitrate of the media object.
        encodingFormat: Media type typically expressed using a MIME format (see [IANA site](http://www.iana.org/assignments/media-types/media-types.xhtml) and [MDN reference](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types)), e.g. application/zip for a SoftwareApplication binary, audio/mpeg for .mp3 etc.

In cases where a [[CreativeWork]] has several media type representations, [[encoding]] can be used to indicate each [[MediaObject]] alongside particular [[encodingFormat]] information.

Unregistered or niche encoding and file formats can be indicated instead via the most appropriate URL, e.g. defining Web page or a Wikipedia/Wikidata entry.
        contentUrl: Actual bytes of the media object, for example the image file or video file.
        associatedArticle: A NewsArticle associated with the Media Object.
        width: The width of the item.
        playerType: Player type required&#x2014;for example, Flash or Silverlight.
        duration: The duration of the item (movie, audio recording, event, etc.) in [ISO 8601 duration format](http://en.wikipedia.org/wiki/ISO_8601).
        embedUrl: A URL pointing to a player for a specific video. In general, this is the information in the ```src``` element of an ```embed``` tag and should not be the same as the content of the ```loc``` tag.
        startTime: The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. E.g. John wrote a book from *January* to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.\
\
Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions.
        ineligibleRegion: The ISO 3166-1 (ISO 3166-1 alpha-2) or ISO 3166-2 code, the place, or the GeoShape for the geo-political region(s) for which the offer or delivery charge specification is not valid, e.g. a region where the transaction is not allowed.\
\
See also [[eligibleRegion]].
      
        sha256: The [SHA-2](https://en.wikipedia.org/wiki/SHA-2) SHA256 hash of the content of the item. For example, a zero-length input has value 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'.
        uploadDate: Date (including time if available) when this media object was uploaded to this site.
    '''
    class_: Literal['https://schema.org/MediaObject'] = Field( # type: ignore
        default='https://schema.org/MediaObject',
        alias='@type',
        serialization_alias='@type'
    )
    encodesCreativeWork: Optional[Union['CreativeWork', List['CreativeWork']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'encodesCreativeWork',
            'https://schema.org/encodesCreativeWork'
        ),
        serialization_alias='https://schema.org/encodesCreativeWork'
    )
    height: Optional[Union['Distance', List['Distance'], 'QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'height',
            'https://schema.org/height'
        ),
        serialization_alias='https://schema.org/height'
    )
    productionCompany: Optional[Union['Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'productionCompany',
            'https://schema.org/productionCompany'
        ),
        serialization_alias='https://schema.org/productionCompany'
    )
    regionsAllowed: Optional[Union['Place', List['Place']]] = Field(
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
    interpretedAsClaim: Optional[Union['Claim', List['Claim']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'interpretedAsClaim',
            'https://schema.org/interpretedAsClaim'
        ),
        serialization_alias='https://schema.org/interpretedAsClaim'
    )
    requiresSubscription: Optional[Union[bool, List[bool], 'MediaSubscription', List['MediaSubscription']]] = Field(
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
    associatedArticle: Optional[Union['NewsArticle', List['NewsArticle']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'associatedArticle',
            'https://schema.org/associatedArticle'
        ),
        serialization_alias='https://schema.org/associatedArticle'
    )
    width: Optional[Union['QuantitativeValue', List['QuantitativeValue'], 'Distance', List['Distance']]] = Field(
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
    duration: Optional[Union['Duration', List['Duration'], 'QuantitativeValue', List['QuantitativeValue']]] = Field(
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
    ineligibleRegion: Optional[Union[str, List[str], 'Place', List['Place'], 'GeoShape', List['GeoShape']]] = Field(
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
