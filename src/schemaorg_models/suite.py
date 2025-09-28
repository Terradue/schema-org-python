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
from .bed_type import BedType
from .bed_details import BedDetails
from .accommodation import Accommodation
from .quantitative_value import QuantitativeValue

class Suite(Accommodation):
    """
A suite in a hotel or other public accommodation, denotes a class of luxury accommodations, the key feature of which is multiple rooms (source: Wikipedia, the free encyclopedia, see <a href="http://en.wikipedia.org/wiki/Suite_(hotel)">http://en.wikipedia.org/wiki/Suite_(hotel)</a>).
<br /><br />
See also the <a href="/docs/hotels.html">dedicated document on the use of schema.org for marking up hotels and other forms of accommodations</a>.

    """
    class_: Literal['https://schema.org/Suite'] = Field( # type: ignore
        default='https://schema.org/Suite',
        alias='@type',
        serialization_alias='@type'
    )
    occupancy: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'occupancy',
            'https://schema.org/occupancy'
        ),
        serialization_alias='https://schema.org/occupancy'
    )
    bed: Optional[Union[BedType, List[BedType], str, List[str], BedDetails, List[BedDetails]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'bed',
            'https://schema.org/bed'
        ),
        serialization_alias='https://schema.org/bed'
    )
    numberOfRooms: Optional[Union[float, List[float], QuantitativeValue, List[QuantitativeValue]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'numberOfRooms',
            'https://schema.org/numberOfRooms'
        ),
        serialization_alias='https://schema.org/numberOfRooms'
    )
