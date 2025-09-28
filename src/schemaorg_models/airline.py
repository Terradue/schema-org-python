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
from .organization import Organization
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .boarding_policy_type import BoardingPolicyType

class Airline(Organization):
    """
An organization that provides flights for passengers.
    """
    class_: Literal['https://schema.org/Airline'] = Field( # type: ignore
        default='https://schema.org/Airline',
        alias='@type',
        serialization_alias='@type'
    )
    iataCode: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'iataCode',
            'https://schema.org/iataCode'
        ),
        serialization_alias='https://schema.org/iataCode'
    )
    boardingPolicy: Optional[Union["BoardingPolicyType", List["BoardingPolicyType"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'boardingPolicy',
            'https://schema.org/boardingPolicy'
        ),
        serialization_alias='https://schema.org/boardingPolicy'
    )
