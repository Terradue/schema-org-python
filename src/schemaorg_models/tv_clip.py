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
from .clip import Clip
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .tv_series import TVSeries

class TVClip(Clip):
    '''
    A short TV program or a segment/part of a TV program.

    Attributes:
        partOfTVSeries: The TV series to which this episode or season belongs.
    '''
    class_: Literal['https://schema.org/TVClip'] = Field( # type: ignore
        default='https://schema.org/TVClip',
        alias='@type',
        serialization_alias='@type'
    )
    partOfTVSeries: Optional[Union['TVSeries', List['TVSeries']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
