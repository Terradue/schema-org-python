from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class MusicAlbumProductionType(Enumeration):
    """
Classification of the album by its type of content: soundtrack, live album, studio album, etc.
    """
    class_: Literal['https://schema.org/MusicAlbumProductionType'] = Field(default='https://schema.org/MusicAlbumProductionType', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
