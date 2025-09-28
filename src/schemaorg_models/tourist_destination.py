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
from .audience import Audience
from .place import Place
from .tourist_attraction import TouristAttraction

class TouristDestination(Place):
    """
A tourist destination. In principle any [[Place]] can be a [[TouristDestination]] from a [[City]], Region or [[Country]] to an [[AmusementPark]] or [[Hotel]]. This Type can be used on its own to describe a general [[TouristDestination]], or be used as an [[additionalType]] to add tourist relevant properties to any other [[Place]].  A [[TouristDestination]] is defined as a [[Place]] that contains, or is colocated with, one or more [[TouristAttraction]]s, often linked by a similar theme or interest to a particular [[touristType]]. The [UNWTO](http://www2.unwto.org/) defines Destination (main destination of a tourism trip) as the place visited that is central to the decision to take the trip.
  (See examples below.)
    """
    class_: Literal['https://schema.org/TouristDestination'] = Field( # type: ignore
        default='https://schema.org/TouristDestination',
        alias='@type',
        serialization_alias='@type'
    )
    touristType: Optional[Union[Audience, List[Audience], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'touristType',
            'https://schema.org/touristType'
        ),
        serialization_alias='https://schema.org/touristType'
    )
    includesAttraction: Optional[Union[TouristAttraction, List[TouristAttraction]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'includesAttraction',
            'https://schema.org/includesAttraction'
        ),
        serialization_alias='https://schema.org/includesAttraction'
    )
