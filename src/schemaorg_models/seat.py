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
from .intangible import Intangible
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .qualitative_value import QualitativeValue

class Seat(Intangible):
    '''
    Used to describe a seat, such as a reserved seat in an event reservation.

    Attributes:
        seatNumber: The location of the reserved seat (e.g., 27).
        seatSection: The section location of the reserved seat (e.g. Orchestra).
        seatingType: The type/class of the seat.
        seatRow: The row location of the reserved seat (e.g., B).
    '''
    class_: Literal['https://schema.org/Seat'] = Field( # type: ignore
        default='https://schema.org/Seat',
        alias='@type',
        serialization_alias='@type'
    )
    seatNumber: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    seatSection: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    seatingType: Optional[Union[str, List[str], 'QualitativeValue', List['QualitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    seatRow: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
