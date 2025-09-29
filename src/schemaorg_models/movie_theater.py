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
from .civic_structure import CivicStructure

class MovieTheater(CivicStructure):
    '''
    A movie theater.

    Attributes:
        screenCount: The number of screens in the movie theater.
    '''
    class_: Literal['https://schema.org/MovieTheater'] = Field( # type: ignore
        default='https://schema.org/MovieTheater',
        alias='@type',
        serialization_alias='@type'
    )
    screenCount: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
