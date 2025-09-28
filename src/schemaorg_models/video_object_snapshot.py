from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.video_object import VideoObject

from pydantic import (
    Field
)
from typing import (
    Literal
)

class VideoObjectSnapshot(VideoObject):
    """
A specific and exact (byte-for-byte) version of a [[VideoObject]]. Two byte-for-byte identical files, for the purposes of this type, considered identical. If they have different embedded metadata the files will differ. Different external facts about the files, e.g. creator or dateCreated that aren't represented in their actual content, do not affect this notion of identity.
    """
    class_: Literal['https://schema.org/VideoObjectSnapshot'] = Field( # type: ignore
        default='https://schema.org/VideoObjectSnapshot',
        alias='@type',
        serialization_alias='@type'
    )
