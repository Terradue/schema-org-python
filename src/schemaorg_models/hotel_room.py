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
from .room import Room
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .bed_type import BedType
    from .quantitative_value import QuantitativeValue
    from .bed_details import BedDetails

class HotelRoom(Room):
    '''
    A hotel room is a single room in a hotel.
<br /><br />
See also the <a href="/docs/hotels.html">dedicated document on the use of schema.org for marking up hotels and other forms of accommodations</a>.


    Attributes:
        occupancy: The allowed total occupancy for the accommodation in persons (including infants etc). For individual accommodations, this is not necessarily the legal maximum but defines the permitted usage as per the contractual agreement (e.g. a double room used by a single person).
Typical unit code(s): C62 for person.
        bed: The type of bed or beds included in the accommodation. For the single case of just one bed of a certain type, you use bed directly with a text.
      If you want to indicate the quantity of a certain kind of bed, use an instance of BedDetails. For more detailed information, use the amenityFeature property.
    '''
    class_: Literal['https://schema.org/HotelRoom'] = Field( # type: ignore
        default='https://schema.org/HotelRoom',
        alias='@type',
        serialization_alias='@type'
    )
    occupancy: Optional[Union['QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'occupancy',
            'https://schema.org/occupancy'
        ),
        serialization_alias='https://schema.org/occupancy'
    )
    bed: Optional[Union['BedType', List['BedType'], str, List[str], 'BedDetails', List['BedDetails']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'bed',
            'https://schema.org/bed'
        ),
        serialization_alias='https://schema.org/bed'
    )
