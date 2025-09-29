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
from .aggregate_rating import AggregateRating

class EmployerAggregateRating(AggregateRating):
    '''
    An aggregate rating of an Organization related to its role as an employer.
    '''
    class_: Literal['https://schema.org/EmployerAggregateRating'] = Field( # type: ignore
        default='https://schema.org/EmployerAggregateRating',
        alias='@type',
        serialization_alias='@type'
    )
