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
from .vehicle import Vehicle
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .quantitative_value import QuantitativeValue

class BusOrCoach(Vehicle):
    """
A bus (also omnibus or autobus) is a road vehicle designed to carry passengers. Coaches are luxury buses, usually in service for long distance travel.
    """
    class_: Literal['https://schema.org/BusOrCoach'] = Field( # type: ignore
        default='https://schema.org/BusOrCoach',
        alias='@type',
        serialization_alias='@type'
    )
    roofLoad: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'roofLoad',
            'https://schema.org/roofLoad'
        ),
        serialization_alias='https://schema.org/roofLoad'
    )
    acrissCode: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'acrissCode',
            'https://schema.org/acrissCode'
        ),
        serialization_alias='https://schema.org/acrissCode'
    )
