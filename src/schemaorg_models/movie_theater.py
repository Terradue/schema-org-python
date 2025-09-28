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
from .civic_structure import CivicStructure

class MovieTheater(CivicStructure):
    """
A movie theater.
    """
    class_: Literal['https://schema.org/MovieTheater'] = Field( # type: ignore
        default='https://schema.org/MovieTheater',
        alias='@type',
        serialization_alias='@type'
    )
    screenCount: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'screenCount',
            'https://schema.org/screenCount'
        ),
        serialization_alias='https://schema.org/screenCount'
    )
