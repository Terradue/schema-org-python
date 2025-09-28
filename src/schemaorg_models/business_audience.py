from __future__ import annotations

from .audience import Audience    

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

class BusinessAudience(Audience):
    """
A set of characteristics belonging to businesses, e.g. who compose an item's target audience.
    """
    class_: Literal['https://schema.org/BusinessAudience'] = Field( # type: ignore
        default='https://schema.org/BusinessAudience',
        alias='@type',
        serialization_alias='@type'
    )
    numberOfEmployees: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'numberOfEmployees',
            'https://schema.org/numberOfEmployees'
        ),
        serialization_alias='https://schema.org/numberOfEmployees'
    )
    yearsInOperation: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'yearsInOperation',
            'https://schema.org/yearsInOperation'
        ),
        serialization_alias='https://schema.org/yearsInOperation'
    )
    yearlyRevenue: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'yearlyRevenue',
            'https://schema.org/yearlyRevenue'
        ),
        serialization_alias='https://schema.org/yearlyRevenue'
    )
