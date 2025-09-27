from typing import Literal
from pydantic import Field
from schemaorg_models.visual_artwork import VisualArtwork


class CoverArt(VisualArtwork):
    """
The artwork on the outer surface of a CreativeWork.
    """
    class_: Literal['https://schema.org/CoverArt'] = Field(default='https://schema.org/CoverArt', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
