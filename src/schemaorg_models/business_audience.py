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
from .audience import Audience
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .quantitative_value import QuantitativeValue

class BusinessAudience(Audience):
    '''
    A set of characteristics belonging to businesses, e.g. who compose an item's target audience.

    Attributes:
        numberOfEmployees: The number of employees in an organization, e.g. business.
        yearsInOperation: The age of the business.
        yearlyRevenue: The size of the business in annual revenue.
    '''
    class_: Literal['https://schema.org/BusinessAudience'] = Field( # type: ignore
        default='https://schema.org/BusinessAudience',
        alias='@type',
        serialization_alias='@type'
    )
    numberOfEmployees: Optional[Union['QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    yearsInOperation: Optional[Union['QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    yearlyRevenue: Optional[Union['QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
