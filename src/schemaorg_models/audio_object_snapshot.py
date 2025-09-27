from typing import Literal
from pydantic import Field
from schemaorg_models.audio_object import AudioObject


class AudioObjectSnapshot(AudioObject):
    """
A specific and exact (byte-for-byte) version of an [[AudioObject]]. Two byte-for-byte identical files, for the purposes of this type, considered identical. If they have different embedded metadata the files will differ. Different external facts about the files, e.g. creator or dateCreated that aren't represented in their actual content, do not affect this notion of identity.
    """
    type_: Literal['https://schema.org/AudioObjectSnapshot'] = Field(default='https://schema.org/AudioObjectSnapshot', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
