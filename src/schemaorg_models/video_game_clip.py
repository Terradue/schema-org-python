from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.clip import Clip


class VideoGameClip(Clip):
    """
A short segment/part of a video game.
    """
    type_: Literal['https://schema.org/VideoGameClip'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/VideoGameClip'),serialization_alias='class') # type: ignore
