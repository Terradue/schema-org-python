from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.aggregate_rating import AggregateRating


class EmployerAggregateRating(AggregateRating):
    """
An aggregate rating of an Organization related to its role as an employer.
    """
    type_: Literal['https://schema.org/EmployerAggregateRating'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/EmployerAggregateRating'),serialization_alias='class') # type: ignore
