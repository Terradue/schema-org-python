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
from .intangible import Intangible
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .qualitative_value import QualitativeValue

class Seat(Intangible):
    """
Used to describe a seat, such as a reserved seat in an event reservation.
    """
    class_: Literal['https://schema.org/Seat'] = Field( # type: ignore
        default='https://schema.org/Seat',
        alias='@type',
        serialization_alias='@type'
    )
    seatNumber: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'seatNumber',
            'https://schema.org/seatNumber'
        ),
        serialization_alias='https://schema.org/seatNumber'
    )
    seatSection: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'seatSection',
            'https://schema.org/seatSection'
        ),
        serialization_alias='https://schema.org/seatSection'
    )
    seatingType: Optional[Union[str, List[str], "QualitativeValue", List["QualitativeValue"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'seatingType',
            'https://schema.org/seatingType'
        ),
        serialization_alias='https://schema.org/seatingType'
    )
    seatRow: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'seatRow',
            'https://schema.org/seatRow'
        ),
        serialization_alias='https://schema.org/seatRow'
    )
