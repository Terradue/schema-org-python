from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.audio_object import AudioObject

from pydantic import (
    Field
)
from typing import (
    Literal
)

class AudioObjectSnapshot(AudioObject):
    """
A specific and exact (byte-for-byte) version of an [[AudioObject]]. Two byte-for-byte identical files, for the purposes of this type, considered identical. If they have different embedded metadata the files will differ. Different external facts about the files, e.g. creator or dateCreated that aren't represented in their actual content, do not affect this notion of identity.
    """
    class_: Literal['https://schema.org/AudioObjectSnapshot'] = Field( # type: ignore
        default='https://schema.org/AudioObjectSnapshot',
        alias='@type',
        serialization_alias='@type'
    )
