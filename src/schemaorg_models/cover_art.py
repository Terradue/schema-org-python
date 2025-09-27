from typing import Literal
from pydantic import Field
from schemaorg_models.visual_artwork import VisualArtwork


class CoverArt(VisualArtwork):
    """
The artwork on the outer surface of a CreativeWork.
    """
    class_: Literal['https://schema.org/CoverArt'] = Field(default='https://schema.org/CoverArt', alias='@type', serialization_alias='@type') # type: ignore
