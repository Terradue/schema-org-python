from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.music_playlist import MusicPlaylist

from schemaorg_models.organization import Organization
from schemaorg_models.music_release_format_type import MusicReleaseFormatType
from schemaorg_models.music_album import MusicAlbum
from schemaorg_models.duration import Duration
from schemaorg_models.quantitative_value import QuantitativeValue
from schemaorg_models.person import Person

class MusicRelease(MusicPlaylist):
    """
A MusicRelease is a specific release of a music album.
    """
    class_: Literal['https://schema.org/MusicRelease'] = Field(default='https://schema.org/MusicRelease', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
    recordLabel: Optional[Union[Organization, List[Organization]]] = Field(default=None, validation_alias=AliasChoices('recordLabel', 'https://schema.org/recordLabel'), serialization_alias='https://schema.org/recordLabel')
    musicReleaseFormat: Optional[Union[MusicReleaseFormatType, List[MusicReleaseFormatType]]] = Field(default=None, validation_alias=AliasChoices('musicReleaseFormat', 'https://schema.org/musicReleaseFormat'), serialization_alias='https://schema.org/musicReleaseFormat')
    catalogNumber: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('catalogNumber', 'https://schema.org/catalogNumber'), serialization_alias='https://schema.org/catalogNumber')
    releaseOf: Optional[Union[MusicAlbum, List[MusicAlbum]]] = Field(default=None, validation_alias=AliasChoices('releaseOf', 'https://schema.org/releaseOf'), serialization_alias='https://schema.org/releaseOf')
    duration: Optional[Union[Duration, List[Duration], QuantitativeValue, List[QuantitativeValue]]] = Field(default=None, validation_alias=AliasChoices('duration', 'https://schema.org/duration'), serialization_alias='https://schema.org/duration')
    creditedTo: Optional[Union[Person, List[Person], Organization, List[Organization]]] = Field(default=None, validation_alias=AliasChoices('creditedTo', 'https://schema.org/creditedTo'), serialization_alias='https://schema.org/creditedTo')
