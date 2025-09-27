from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class IncentiveQualifiedExpenseType(Enumeration):
    """
The types of expenses that are covered by the incentive. For example some incentives are only for the goods (tangible items) but the services (labor) are excluded.
    """
    class_: Literal['https://schema.org/IncentiveQualifiedExpenseType'] = Field(default='https://schema.org/IncentiveQualifiedExpenseType', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
