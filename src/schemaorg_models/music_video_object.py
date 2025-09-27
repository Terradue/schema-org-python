from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.media_object import MediaObject


class MusicVideoObject(MediaObject):
    """
A music video file.
    """
    type_: Literal['https://schema.org/MusicVideoObject'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/MusicVideoObject'),serialization_alias='class') # type: ignore
