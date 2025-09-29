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
from .trip import Trip
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .audience import Audience

class TouristTrip(Trip):
    '''
    A tourist trip. A created itinerary of visits to one or more places of interest ([[TouristAttraction]]/[[TouristDestination]]) often linked by a similar theme, geographic area, or interest to a particular [[touristType]]. The [UNWTO](http://www2.unwto.org/) defines tourism trip as the Trip taken by visitors.
  (See examples below.)

    Attributes:
        touristType: Attraction suitable for type(s) of tourist. E.g. children, visitors from a particular country, etc. 
    '''
    class_: Literal['https://schema.org/TouristTrip'] = Field( # type: ignore
        default='https://schema.org/TouristTrip',
        alias='@type',
        serialization_alias='@type'
    )
    touristType: Optional[Union['Audience', List['Audience'], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'touristType',
            'https://schema.org/touristType'
        ),
        serialization_alias='https://schema.org/touristType'
    )
