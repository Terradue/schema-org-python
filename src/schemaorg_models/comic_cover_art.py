from __future__ import annotations
from datetime import (
    date,
    datetime,
    time
)
from pydantic import (
    field_serializer,
    field_validator,
    AliasChoices,
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .comic_story import ComicStory

class ComicCoverArt(ComicStory):
    '''
    The artwork on the cover of a comic.
    '''
    class_: Literal['https://schema.org/ComicCoverArt'] = Field( # type: ignore
        default='https://schema.org/ComicCoverArt',
        alias='@type',
        serialization_alias='@type'
    )
