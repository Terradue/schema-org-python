from typing import Literal
from pydantic import Field
from schemaorg_models.aggregate_rating import AggregateRating


class EmployerAggregateRating(AggregateRating):
    """
An aggregate rating of an Organization related to its role as an employer.
    """
    class_: Literal['https://schema.org/EmployerAggregateRating'] = Field(default='https://schema.org/EmployerAggregateRating', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
