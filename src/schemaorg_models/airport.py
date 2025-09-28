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
from .civic_structure import CivicStructure

class Airport(CivicStructure):
    """
An airport.
    """
    class_: Literal['https://schema.org/Airport'] = Field( # type: ignore
        default='https://schema.org/Airport',
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
    icaoCode: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'icaoCode',
            'https://schema.org/icaoCode'
        ),
        serialization_alias='https://schema.org/icaoCode'
    )
