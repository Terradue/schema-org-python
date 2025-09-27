from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class MusicReleaseFormatType(Enumeration):
    """
Format of this release (the type of recording media used, i.e. compact disc, digital media, LP, etc.).
    """
    class_: Literal['https://schema.org/MusicReleaseFormatType'] = Field(default='https://schema.org/MusicReleaseFormatType', alias='@type', serialization_alias='@type') # type: ignore
