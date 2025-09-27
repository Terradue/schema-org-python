from typing import Literal
from pydantic import Field
from schemaorg_models.aggregate_rating import AggregateRating


class EmployerAggregateRating(AggregateRating):
    """
An aggregate rating of an Organization related to its role as an employer.
    """
    class_: Literal['https://schema.org/EmployerAggregateRating'] = Field('class', alias='class', serialization_alias='class') # type: ignore
