from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.media_object import MediaObject


class AmpStory(MediaObject):
    """
A creative work with a visual storytelling format intended to be viewed online, particularly on mobile devices.
    """
    type_: Literal['https://schema.org/AmpStory'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/AmpStory'),serialization_alias='class') # type: ignore
