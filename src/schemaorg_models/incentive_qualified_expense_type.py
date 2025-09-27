from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class IncentiveQualifiedExpenseType(Enumeration):
    """
The types of expenses that are covered by the incentive. For example some incentives are only for the goods (tangible items) but the services (labor) are excluded.
    """
    type_: Literal['https://schema.org/IncentiveQualifiedExpenseType'] = Field(default='https://schema.org/IncentiveQualifiedExpenseType', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
