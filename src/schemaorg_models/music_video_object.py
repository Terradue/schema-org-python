from typing import Literal
from pydantic import Field
from schemaorg_models.media_object import MediaObject


class MusicVideoObject(MediaObject):
    """
A music video file.
    """
    class_: Literal['https://schema.org/MusicVideoObject'] = Field(default='https://schema.org/MusicVideoObject', alias='@type', serialization_alias='@type') # type: ignore
