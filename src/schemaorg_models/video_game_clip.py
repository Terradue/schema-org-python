from typing import Literal
from pydantic import Field
from schemaorg_models.clip import Clip


class VideoGameClip(Clip):
    """
A short segment/part of a video game.
    """
    class_: Literal['https://schema.org/VideoGameClip'] = Field('class', alias='class', serialization_alias='class') # type: ignore
