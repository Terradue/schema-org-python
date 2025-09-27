from typing import Literal
from pydantic import Field
from schemaorg_models.aggregate_rating import AggregateRating


class EmployerAggregateRating(AggregateRating):
    """
An aggregate rating of an Organization related to its role as an employer.
    """
    type_: Literal['https://schema.org/EmployerAggregateRating'] = Field(default='https://schema.org/EmployerAggregateRating', alias='@type', serialization_alias='@type') # type: ignore
