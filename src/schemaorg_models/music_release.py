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
    from .quantitative_value import QuantitativeValue
    from .duration import Duration
    from .organization import Organization
    from .music_album import MusicAlbum

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
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    musicReleaseFormat: Optional[Union['MusicReleaseFormatType', List['MusicReleaseFormatType']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    catalogNumber: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    releaseOf: Optional[Union['MusicAlbum', List['MusicAlbum']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    duration: Optional[Union['Duration', List['Duration'], 'QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    creditedTo: Optional[Union['Person', List['Person'], 'Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
