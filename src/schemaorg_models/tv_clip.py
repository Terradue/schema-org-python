from __future__ import annotations
from pydantic import (
    AliasChoices,
    Field
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .tv_series import TVSeries
from .clip import Clip

class TVClip(Clip):
    """
A short TV program or a segment/part of a TV program.
    """
    class_: Literal['https://schema.org/TVClip'] = Field( # type: ignore
        default='https://schema.org/TVClip',
        alias='@type',
        serialization_alias='@type'
    )
    partOfTVSeries: Optional[Union[TVSeries, List[TVSeries]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'partOfTVSeries',
            'https://schema.org/partOfTVSeries'
        ),
        serialization_alias='https://schema.org/partOfTVSeries'
    )
