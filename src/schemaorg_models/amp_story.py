from typing import Literal
from pydantic import Field
from schemaorg_models.media_object import MediaObject


class AmpStory(MediaObject):
    """
A creative work with a visual storytelling format intended to be viewed online, particularly on mobile devices.
    """
    type_: Literal['https://schema.org/AmpStory'] = Field(default='https://schema.org/AmpStory', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
