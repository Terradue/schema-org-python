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
from .accommodation import Accommodation
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .quantitative_value import QuantitativeValue

class Apartment(Accommodation):
    '''
    An apartment (in American English) or flat (in British English) is a self-contained housing unit (a type of residential real estate) that occupies only part of a building (source: Wikipedia, the free encyclopedia, see <a href="http://en.wikipedia.org/wiki/Apartment">http://en.wikipedia.org/wiki/Apartment</a>).

    Attributes:
        occupancy: The allowed total occupancy for the accommodation in persons (including infants etc). For individual accommodations, this is not necessarily the legal maximum but defines the permitted usage as per the contractual agreement (e.g. a double room used by a single person).
Typical unit code(s): C62 for person.
        numberOfRooms: The number of rooms (excluding bathrooms and closets) of the accommodation or lodging business.
Typical unit code(s): ROM for room or C62 for no unit. The type of room can be put in the unitText property of the QuantitativeValue.
    '''
    class_: Literal['https://schema.org/Apartment'] = Field( # type: ignore
        default='https://schema.org/Apartment',
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
    numberOfRooms: Optional[Union[float, List[float], 'QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'numberOfRooms',
            'https://schema.org/numberOfRooms'
        ),
        serialization_alias='https://schema.org/numberOfRooms'
    )
