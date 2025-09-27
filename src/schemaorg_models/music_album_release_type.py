from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class MusicAlbumReleaseType(Enumeration):
    """
The kind of release which this album is: single, EP or album.
    """
    class_: Literal['https://schema.org/MusicAlbumReleaseType'] = Field(default='https://schema.org/MusicAlbumReleaseType', alias='class', serialization_alias='class') # type: ignore
