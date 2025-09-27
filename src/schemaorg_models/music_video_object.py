from typing import Literal
from pydantic import Field
from schemaorg_models.media_object import MediaObject


class MusicVideoObject(MediaObject):
    """
A music video file.
    """
    type_: Literal['https://schema.org/MusicVideoObject'] = Field(default='https://schema.org/MusicVideoObject', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
