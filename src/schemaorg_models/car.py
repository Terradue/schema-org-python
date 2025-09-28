from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.vehicle import Vehicle

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

class Car(Vehicle):
    """
A car is a wheeled, self-powered motor vehicle used for transportation.
    """
    class_: Literal['https://schema.org/Car'] = Field( # type: ignore
        default='https://schema.org/Car',
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
