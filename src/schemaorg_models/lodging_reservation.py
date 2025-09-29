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
from .reservation import Reservation
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .qualitative_value import QualitativeValue
    from .quantitative_value import QuantitativeValue

class LodgingReservation(Reservation):
    '''
    A reservation for lodging at a hotel, motel, inn, etc.\
\
Note: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations.

    Attributes:
        checkoutTime: The latest someone may check out of a lodging establishment.
        numAdults: The number of adults staying in the unit.
        checkinTime: The earliest someone may check into a lodging establishment.
        lodgingUnitType: Textual description of the unit type (including suite vs. room, size of bed, etc.).
        lodgingUnitDescription: A full description of the lodging unit.
        numChildren: The number of children staying in the unit.
    '''
    class_: Literal['https://schema.org/LodgingReservation'] = Field( # type: ignore
        default='https://schema.org/LodgingReservation',
        alias='@type',
        serialization_alias='@type'
    )
    checkoutTime: Optional[Union[datetime, List[datetime], time, List[time]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'checkoutTime',
            'https://schema.org/checkoutTime'
        ),
        serialization_alias='https://schema.org/checkoutTime'
    )
    numAdults: Optional[Union['QuantitativeValue', List['QuantitativeValue'], int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'numAdults',
            'https://schema.org/numAdults'
        ),
        serialization_alias='https://schema.org/numAdults'
    )
    checkinTime: Optional[Union[time, List[time], datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'checkinTime',
            'https://schema.org/checkinTime'
        ),
        serialization_alias='https://schema.org/checkinTime'
    )
    lodgingUnitType: Optional[Union[str, List[str], 'QualitativeValue', List['QualitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'lodgingUnitType',
            'https://schema.org/lodgingUnitType'
        ),
        serialization_alias='https://schema.org/lodgingUnitType'
    )
    lodgingUnitDescription: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'lodgingUnitDescription',
            'https://schema.org/lodgingUnitDescription'
        ),
        serialization_alias='https://schema.org/lodgingUnitDescription'
    )
    numChildren: Optional[Union['QuantitativeValue', List['QuantitativeValue'], int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'numChildren',
            'https://schema.org/numChildren'
        ),
        serialization_alias='https://schema.org/numChildren'
    )
