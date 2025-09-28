from __future__ import annotations

from .aggregate_rating import AggregateRating    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class EmployerAggregateRating(AggregateRating):
    """
An aggregate rating of an Organization related to its role as an employer.
    """
    class_: Literal['https://schema.org/EmployerAggregateRating'] = Field( # type: ignore
        default='https://schema.org/EmployerAggregateRating',
        alias='@type',
        serialization_alias='@type'
    )
