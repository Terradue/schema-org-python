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
    from .bed_type import BedType

class BedDetails(Intangible):
    '''
    An entity holding detailed information about the available bed types, e.g. the quantity of twin beds for a hotel room. For the single case of just one bed of a certain type, you can use bed directly with a text. See also [[BedType]] (under development).

    Attributes:
        typeOfBed: The type of bed to which the BedDetail refers, i.e. the type of bed available in the quantity indicated by quantity.
        numberOfBeds: The quantity of the given bed type available in the HotelRoom, Suite, House, or Apartment.
    '''
    class_: Literal['https://schema.org/BedDetails'] = Field( # type: ignore
        default='https://schema.org/BedDetails',
        alias='@type',
        serialization_alias='@type'
    )
    typeOfBed: Optional[Union['BedType', List['BedType'], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'typeOfBed',
            'https://schema.org/typeOfBed'
        ),
        serialization_alias='https://schema.org/typeOfBed'
    )
    numberOfBeds: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'numberOfBeds',
            'https://schema.org/numberOfBeds'
        ),
        serialization_alias='https://schema.org/numberOfBeds'
    )
