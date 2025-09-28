from __future__ import annotations

from .organization import Organization    

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
