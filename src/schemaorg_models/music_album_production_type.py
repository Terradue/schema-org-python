from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class MusicAlbumProductionType(Enumeration):
    """
Classification of the album by its type of content: soundtrack, live album, studio album, etc.
    """
    type_: Literal['https://schema.org/MusicAlbumProductionType'] = Field(default='https://schema.org/MusicAlbumProductionType', alias='@type', serialization_alias='@type') # type: ignore
