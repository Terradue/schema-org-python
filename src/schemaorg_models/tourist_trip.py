from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.trip import Trip

from schemaorg_models.audience import Audience

class TouristTrip(Trip):
    """
A tourist trip. A created itinerary of visits to one or more places of interest ([[TouristAttraction]]/[[TouristDestination]]) often linked by a similar theme, geographic area, or interest to a particular [[touristType]]. The [UNWTO](http://www2.unwto.org/) defines tourism trip as the Trip taken by visitors.
  (See examples below.)
    """
    type_: Literal['https://schema.org/TouristTrip'] = Field(default='https://schema.org/TouristTrip', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
    touristType: Optional[Union[Audience, List[Audience], str, List[str]]] = Field(default=None, validation_alias=AliasChoices('touristType', 'https://schema.org/touristType'), serialization_alias='https://schema.org/touristType')
