from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.reservation import Reservation

from datetime import (
    datetime,
    time
)
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
from schemaorg_models.quantitative_value import QuantitativeValue

class FoodEstablishmentReservation(Reservation):
    """
A reservation to dine at a food-related business.\
\
Note: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations.
    """
    class_: Literal['https://schema.org/FoodEstablishmentReservation'] = Field( # type: ignore
        default='https://schema.org/FoodEstablishmentReservation',
        alias='@type',
        serialization_alias='@type'
    )
    partySize: Optional[Union[int, List[int], QuantitativeValue, List[QuantitativeValue]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'partySize',
            'https://schema.org/partySize'
        ),
        serialization_alias='https://schema.org/partySize'
    )
    endTime: Optional[Union[time, List[time], datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'endTime',
            'https://schema.org/endTime'
        ),
        serialization_alias='https://schema.org/endTime'
    )
    startTime: Optional[Union[time, List[time], datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'startTime',
            'https://schema.org/startTime'
        ),
        serialization_alias='https://schema.org/startTime'
    )
