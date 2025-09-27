from typing import Literal
from pydantic import Field
from schemaorg_models.clip import Clip


class VideoGameClip(Clip):
    """
A short segment/part of a video game.
    """
    type_: Literal['https://schema.org/VideoGameClip'] = Field(default='https://schema.org/VideoGameClip', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
