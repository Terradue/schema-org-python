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
from .civic_structure import CivicStructure

class Airport(CivicStructure):
    '''
    An airport.

    Attributes:
        iataCode: IATA identifier for an airline or airport.
        icaoCode: ICAO identifier for an airport.
    '''
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
