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
from .music_playlist import MusicPlaylist
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .person import Person
    from .music_release_format_type import MusicReleaseFormatType
    from .duration import Duration
    from .quantitative_value import QuantitativeValue
    from .music_album import MusicAlbum
    from .organization import Organization

class MusicRelease(MusicPlaylist):
    '''
    A MusicRelease is a specific release of a music album.

    Attributes:
        recordLabel: The label that issued the release.
        musicReleaseFormat: Format of this release (the type of recording media used, i.e. compact disc, digital media, LP, etc.).
        catalogNumber: The catalog number for the release.
        releaseOf: The album this is a release of.
        duration: The duration of the item (movie, audio recording, event, etc.) in [ISO 8601 duration format](http://en.wikipedia.org/wiki/ISO_8601).
        creditedTo: The group the release is credited to if different than the byArtist. For example, Red and Blue is credited to "Stefani Germanotta Band", but by Lady Gaga.
    '''
    class_: Literal['https://schema.org/MusicRelease'] = Field( # type: ignore
        default='https://schema.org/MusicRelease',
        alias='@type',
        serialization_alias='@type'
    )
    recordLabel: Optional[Union['Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'recordLabel',
            'https://schema.org/recordLabel'
        ),
        serialization_alias='https://schema.org/recordLabel'
    )
    musicReleaseFormat: Optional[Union['MusicReleaseFormatType', List['MusicReleaseFormatType']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'musicReleaseFormat',
            'https://schema.org/musicReleaseFormat'
        ),
        serialization_alias='https://schema.org/musicReleaseFormat'
    )
    catalogNumber: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'catalogNumber',
            'https://schema.org/catalogNumber'
        ),
        serialization_alias='https://schema.org/catalogNumber'
    )
    releaseOf: Optional[Union['MusicAlbum', List['MusicAlbum']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'releaseOf',
            'https://schema.org/releaseOf'
        ),
        serialization_alias='https://schema.org/releaseOf'
    )
    duration: Optional[Union['Duration', List['Duration'], 'QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'duration',
            'https://schema.org/duration'
        ),
        serialization_alias='https://schema.org/duration'
    )
    creditedTo: Optional[Union['Person', List['Person'], 'Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'creditedTo',
            'https://schema.org/creditedTo'
        ),
        serialization_alias='https://schema.org/creditedTo'
    )
