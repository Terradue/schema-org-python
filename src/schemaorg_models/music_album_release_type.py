from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class MusicAlbumReleaseType(Enumeration):
    """
The kind of release which this album is: single, EP or album.
    """
    type_: Literal['https://schema.org/MusicAlbumReleaseType'] = Field(default='https://schema.org/MusicAlbumReleaseType', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
