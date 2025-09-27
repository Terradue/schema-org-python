from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.enumeration import Enumeration


class MusicAlbumReleaseType(Enumeration):
    """
The kind of release which this album is: single, EP or album.
    """
    type_: Literal['https://schema.org/MusicAlbumReleaseType'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/MusicAlbumReleaseType'),serialization_alias='class') # type: ignore
