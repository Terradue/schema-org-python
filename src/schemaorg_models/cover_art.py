from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.visual_artwork import VisualArtwork


class CoverArt(VisualArtwork):
    """
The artwork on the outer surface of a CreativeWork.
    """
    type_: Literal['https://schema.org/CoverArt'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/CoverArt'),serialization_alias='class') # type: ignore
