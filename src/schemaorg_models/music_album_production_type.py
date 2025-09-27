from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.enumeration import Enumeration


class MusicAlbumProductionType(Enumeration):
    """
Classification of the album by its type of content: soundtrack, live album, studio album, etc.
    """
    type_: Literal['https://schema.org/MusicAlbumProductionType'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/MusicAlbumProductionType'),serialization_alias='class') # type: ignore
