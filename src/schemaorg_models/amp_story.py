from typing import Literal
from pydantic import Field
from schemaorg_models.media_object import MediaObject


class AmpStory(MediaObject):
    """
A creative work with a visual storytelling format intended to be viewed online, particularly on mobile devices.
    """
    class_: Literal['https://schema.org/AmpStory'] = Field('class', alias='class', serialization_alias='class') # type: ignore
